from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.db.models import Q
from datetime import datetime
from .payment import paypal_payment

from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.measure import Distance

from rest_framework import viewsets, filters

from users.models import User
from rentals.models import Transaction
from .models import (Category, CategoryProperty, Gear, GearProperty, Location,
    GearAvailability, GearImage)
from .serializers import (CategorySerializer, CategoryPropertySerializer,
    GearSerializer, GearPropertySerializer,
    LocationSerializer, GearAvailabilitySerializer,
    GearImageSerializer)


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

    # def contact_method(self, method):
    #     if method == 0:
    #         return "Phone"
    #     else:
    #         return "Email"

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
        categories = gear.categories.values()
        category_list = []
        for category in categories:
            category_list.append((category['name'] + ", " + category['description']))
        gear_properties = GearProperty.objects.filter(gear=gear)
        payments = self.convert_payment_method(gear.payment)
        #contact = self.contact_method(gear.preferred_contact)
        context = {
            "name": gear.name,
            "description": gear.description,
            "categories": category_list,
            "brand": gear.brand,
            "price": gear.price,
            #"preferred_contact": contact,
            "payments": payments,
            "expiration_date": gear.expiration_date,
            "photo": photo.photo.url,
            "user": gear.user,
            "location": gear.location.address,
            "gear_properties": gear_properties,
            "renters_email": renters_email,
            "renters_phone":renters_phone,
        }
        print(gear.expiration_date)
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
        cancel_return_address = "http://localhost:8000" + request.get_full_path()
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
        category_id = request.POST["frmCategorySelect"]
        category = Category.object.get(id=category_id)

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








# Following views for API endpoints
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class CategoryPropertyViewSet(viewsets.ModelViewSet):
    queryset = CategoryProperty.objects.all().order_by("name")
    serializer_class = CategoryPropertySerializer


class GearViewSet(viewsets.ModelViewSet):
    queryset = Gear.objects.all().order_by("name")
    serializer_class = GearSerializer


class GearPropertyViewSet(viewsets.ModelViewSet):
    queryset = GearProperty.objects.all()
    serializer_class = GearPropertySerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ("address",)

    def get_queryset(self):
        query_params = Q()
        categories_params = Q()
        exclude_dates_params = Q()

        categories = self.request.query_params.getlist('categories[]')
        latitude = (self.request.query_params.get('lat'))
        longitude = (self.request.query_params.get('lng'))
        distance = (self.request.query_params.get('miles'))
        min_price = (self.request.query_params.get('minPrice'))
        max_price = (self.request.query_params.get('maxPrice'))
        start_date = (self.request.query_params.get('startDate'))
        end_date = (self.request.query_params.get('endDate'))
        gear = (self.request.query_params.get('gear'))
        user = (self.request.query_params.get('user'))

        if latitude and longitude and distance:
            center = fromstr("POINT({} {})".format(latitude, longitude))
            distance_from_point = {'mi': distance}
            query_params.add(Q(point__distance_lte=(center, Distance(**distance_from_point))), query_params.connector)
        if min_price:
            query_params.add(Q(gear__price__gte=min_price), query_params.connector)
        if max_price:
            query_params.add(Q(gear__price__lte=max_price), query_params.connector)
        if gear:
            query_params.add(Q(gear__id=gear), query_params.connector)
        if user:
            query_params.add(Q(gear__user__id=user), query_params.connector)

        if start_date:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            exclude_dates_params.add(Q(gear__gearavailability__not_available_date__gte=start), query_params.connector)
        if end_date:
            end = datetime.strptime(end_date, "%Y-%m-%d")
            exclude_dates_params.add(Q(gear__gearavailability__not_available_date__lte=end), query_params.connector)

        for i in categories:
            categories_params.add(Q(gear__categories__id=i), categories_params.OR)

        queryset = self.queryset.filter(query_params).filter(categories_params).exclude(exclude_dates_params)#.distance(center).order_by('distance')
        return queryset


class GearAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = GearAvailability.objects.all()
    serializer_class = GearAvailabilitySerializer


class GearImageViewSet(viewsets.ModelViewSet):
    queryset = GearImage.objects.all()
    serializer_class = GearImageSerializer
