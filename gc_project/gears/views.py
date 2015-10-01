from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.db.models import Q

from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.measure import Distance

from rest_framework import viewsets, filters

from .models import (Category, CategoryProperty, Gear, GearProperty, Location,
    GearAvailability, GearImage)
from .serializers import (CategorySerializer, CategoryPropertySerializer,
    GearSerializer, GearPropertySerializer,
    LocationSerializer, GearAvailabilitySerializer,
    GearImageSerializer)


class HomeView(View):
    def get(self, request):
        return render(request, 'gears/home.html')

from .forms import RentalForm

class GearView(View):
    def payment_method(self, method):
        if method == 0:
            return "Cash"
        elif method == 1:
            return "PayPal"
        else:
            return "Cash or PayPal"

    def contact_method(self, method):
        if method == 0:
            return "Phone"
        else:
            return "Email"

    def get(self, request, gear_id):
        gear = Gear.objects.get(id=gear_id)
        photo = GearImage.objects.get(gear=gear)
        categories = gear.categories.values()
        category_list = []
        for category in categories:
            category_list.append((category['name'] + ", " + category['description']))
        gear_properties = GearProperty.objects.filter(gear=gear)
        payment = self.payment_method(gear.payment)
        contact = self.contact_method(gear.preferred_contact)
        context = {
            "name": gear.name,
            "description": gear.description,
            "categories": category_list,
            "brand": gear.brand,
            "price": gear.price,
            "preferred_contact": contact,
            "payment": payment,
            "expiration_date": gear.expiration_date,
            "photo": photo.photo.url,
            "user": gear.user,
            "location": gear.location.address,
            "gear_properties": gear_properties,
            "form": RentalForm()
        }

        return render(request, 'gears/gear.html', context)

    def post(self, request):
        pass
#         recipient_email =
#         days_rented =
#         dollars = days_rented * <dollars per day>
#         cancel_return_address = <this is the current address>
#         paypal_redirect_address = paypal_payment(recipient_email, dollars, cancel_return_address)
#         return redirect(paypal_redirect_address)


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
        return HttpResponse("ADD stuff")

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
        print("QUERY STRING = {}".format(self.request.query_params))
        print("CATEGORIES WITH GET LIST = {}".format(self.request.query_params.getlist('categories[]')))
        print("CATEGORIES WITH GET = {}".format(self.request.GET.get('categories[]')))
        query_params = Q()
        latitude = (self.request.query_params.get('lat'))
        longitude = (self.request.query_params.get('lng'))
        distance = (self.request.query_params.get('miles'))
        category = (self.request.query_params.get('category'))
        #price = (self.request.query_params.get('price'))
        gear = (self.request.query_params.get('gear'))
        user = (self.request.query_params.get('user'))
        if latitude and longitude and distance:
            center = fromstr("POINT({} {})".format(latitude, longitude))
            distance_from_point = {'mi': distance}
            query_params.add(Q(point__distance_lte=(center, Distance(**distance_from_point))), query_params.connector)

            query_params.add(Q(address='new york'), query_params.connector)
        if category:
            query_params.add(Q(gear__categories__name=category), query_params.connector)
        # if price:
        #     query_params.add(Q(gear__categories__name=category), query_params.connector)
        if gear:
            query_params.add(Q(gear__id=gear), query_params.connector)
        if user:
            query_params.add(Q(gear__user__id=user), query_params.connector)
            #for key, val in options.items():
                #qs.add(Q(attributes__name=key) & Q(attribute_values__value_option__option=val), qs.connector)

            #queryset = self.queryset.filter(
            #point__distance_lte=(center, Distance(**distance_from_point)),
            #address="boston",
            #gear__price=100,
            #    query_params
            #).distance(center).order_by('distance')
        #else:
            #queryset = self.queryset.filter()
        queryset = self.queryset.filter(query_params)#.distance(center).order_by('distance')
        return queryset


class GearAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = GearAvailability.objects.all()
    serializer_class = GearAvailabilitySerializer


class GearImageViewSet(viewsets.ModelViewSet):
    queryset = GearImage.objects.all()
    serializer_class = GearImageSerializer
