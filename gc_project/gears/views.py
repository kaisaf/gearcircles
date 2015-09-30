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

from datetime import datetime


class HomeView(View):
    def get(self, request):
        return render(request, 'gears/home.html')


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
        query_params = Q()
        categories_params = Q()
        
        categories = self.request.query_params.getlist('categories[]')
        latitude = (self.request.query_params.get('lat'))
        longitude = (self.request.query_params.get('lng'))
        distance = (self.request.query_params.get('miles'))
        min_price = (self.request.query_params.get('minPrice'))
        max_price = (self.request.query_params.get('maxPrice'))
        available_date = (self.request.query_params.get('startDate'))
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
        if available_date:
            d = datetime.strptime(available_date, "%Y-%m-%d")
            print(d)
            query_params.add(Q(gear__gearavailability__id = 3))
            print("passed")
        if gear:
            query_params.add(Q(gear__id=gear), query_params.connector)
        if user:
            query_params.add(Q(gear__user__id=user), query_params.connector)
        for i in categories:
            categories_params.add(Q(gear__categories__id=i), categories_params.OR)
            
        print(query_params)
        print(categories_params)
        queryset = self.queryset.filter(query_params).filter(categories_params)#.distance(center).order_by('distance')
        return queryset


class GearAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = GearAvailability.objects.all()
    serializer_class = GearAvailabilitySerializer


class GearImageViewSet(viewsets.ModelViewSet):
    queryset = GearImage.objects.all()
    serializer_class = GearImageSerializer
