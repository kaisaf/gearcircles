from rest_framework import viewsets, filters

from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.measure import Distance

from django.db.models import Q

from datetime import datetime

from .serializers import (CategorySerializer, CategoryPropertySerializer,
    GearSerializer, GearPropertySerializer,
    LocationSerializer, GearAvailabilitySerializer,
    GearImageSerializer)

from users.models import User
from rentals.models import Transaction
from .models import (Category, CategoryProperty, Gear, GearProperty, Location,
    GearAvailability, GearImage)




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