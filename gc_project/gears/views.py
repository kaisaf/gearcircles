from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import View
from datetime import datetime
from random import randint
from .payment import paypal_payment

from django.contrib.gis.geos import Point, fromstr

from users.models import User
from rentals.models import Transaction
from rentals import twilio_helper
from .models import (Category, CategoryProperty, Gear, GearProperty, Location,
    GearAvailability, GearImage)


class HomeView(View):
    def get(self, request):
        return render(request, 'gears/home.html')


class GearView(View):
    def convert_payment_method(self, method):
        if method == 0:
            return ["Cash"]
        elif method == 1:
            return ["PayPal"]
        elif method == "Cash":
            return 0
        elif method == "PayPal":
            return 1
        else:
            return ["PayPal", "Cash"]

    def create_transaction(self, start_date, end_date, gear, borrower_user, price_paid, payment_method):
        Transaction.objects.create(
            start_date = start_date,
            end_date = end_date,
            gear = gear,
            owner_user = gear.user,
            borrower_user = borrower_user,
            price_paid = price_paid,
            payment_method = payment_method
        )

    def get_gear_object(self, gear_id):
        return Gear.objects.get(id=gear_id)

    def get(self, request, gear_id):
        renters_email = request.user.email
        renters_phone = request.user.phone
        gear = self.get_gear_object(gear_id)
        photo = GearImage.objects.get(gear=gear)
        category = gear.category.name
        gear_properties = GearProperty.objects.filter(gear=gear)
        payments = self.convert_payment_method(gear.payment)
        context = {
            "id": gear.id,
            "name": gear.name,
            "description": gear.description,
            "category": category,
            "brand": gear.brand,
            "price": gear.price,
            "payments": payments,
            "expiration_date": gear.expiration_date,
            "photo": photo.photo.url,
            "user": gear.user,
            "location": gear.location.address,
            "gear_properties": gear_properties,
            "renters_email": renters_email,
            "renters_phone":renters_phone,
        }
        return render(request, 'gears/gear.html', context)

    def post(self, request, gear_id):
        gear = self.get_gear_object(gear_id)
        recipient_email = gear.user.email
        start_date = request.POST["startDate"]
        end_date = request.POST["endDate"]
        phone = request.POST["myPhone"]
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        days_rented = (end_date - start_date).days + 1
        dollars = days_rented * gear.price
        payment_method = request.POST["paymentMethod"]
        cancel_return_address = "http://www.gearcircles.com/myaccount"
        renter = User.objects.get(id=request.user.id)
        if not request.user.phone or renter.phone != phone:
            renter.phone = phone
            renter.save()
        self.create_transaction(start_date, end_date, gear, renter, dollars, self.convert_payment_method(payment_method))
        if payment_method == "PayPal":
            paypal_redirect_address = paypal_payment(recipient_email, dollars, cancel_return_address)
            return redirect(paypal_redirect_address)
        else:
            return redirect('myaccount')

class CreateCodeView(View):
    def post(self, request):
        phone = request.POST["phone"]
        code = str(randint(1000, 9999))
        message = "Your PIN code is: " + code
        request.session["code"] = code
        twilio_helper.send_sms(phone, message)
        return HttpResponse("Message sent")

class ValidateCodeView(View):
    def post(self, request):
        if request.POST["pin"] == request.session["code"]:
            return HttpResponse("PIN correct!")
        else:
            raise Http404("Wrong PIN")

class CategoriesView(View):
    def get(self, request):
        return HttpResponse("Gear CategoryView")


class CategoryByNameView(View):
    def get(self, request, category_name):
        return HttpResponse("Gear CategoryByNameView " + category_name)


class LocationsView(View):
    def get(self, request):
        return HttpResponse("Gear Locations")


class LocationByNameView(View):
    def get(self, request, location_name):
        return HttpResponse("Gear Locations by loc name " + location_name)


class AddGearView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            "categories": categories,
        }
        return render(request, 'gears/addgear.html', context)

    def post(self, request):
        user = User.objects.get(email=request.user.email)
        phone = request.POST["frmPhone"]
        category_id = request.POST["frmCategorySelect"]
        category = Category.objects.get(id=category_id)

        address = request.POST["frmAddress"]
        latitude = request.POST["frmLatitude"]
        longitude = request.POST["frmLongitude"]
        point = fromstr("POINT({} {})".format(longitude, latitude))
        location = Location.objects.create(address=address, point=point)

        name = request.POST["frmName"]
        description = request.POST["frmDescription"]
        brand = request.POST["frmBrand"]
        price = request.POST["frmPrice"]
        payment = request.POST["frmPayment"]
        expiration_date = request.POST["frmDate"]

        new_gear = Gear.objects.create(
            name=name,
            description=description,
            brand=brand,
            price=price,
            preferred_contact = 0,
            payment=payment,
            expiration_date=expiration_date,
            category=category,
            user=user,
            location=location
        )

        category_properties = CategoryProperty.objects.filter(category=category)
        for category_property in category_properties:
            insert_gear_property(new_gear, category_property, request)

        new_gear_image = GearImage.objects.create(
            gear=new_gear,
            photo = request.FILES['frmImage']
        )

        return redirect('myaccount')

def insert_gear_property(new_gear, category_property, request):
    frm_input_name = "frm{}".format(category_property.id)
    value = request.POST.get(frm_input_name)
    if value:
        new_property = GearProperty.objects.create(
            value=value,
            gear=new_gear,
            category_property=category_property
        )
