from rest_framework import serializers
from .models import Category, CategoryProperty, Gear, GearProperty, Location, GearAvailability, GearImage
from users.serializers import UserSerializer


class CategoryPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProperty
        fields = ('id', 'name', 'description', 'mandatory', 'input_type')


class CategorySerializer(serializers.ModelSerializer):
    categoryproperty_set = CategoryPropertySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'categoryproperty_set')


class GearPropertySerializer(serializers.ModelSerializer):
    category_property = CategoryPropertySerializer(read_only=True)
    class Meta:
        model = GearProperty
        fields = ('value', 'gear', 'category_property')


class GearAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = GearAvailability
        fields = ('id', 'not_available_date', 'gear')


class GearImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearImage
        fields = ('photo', 'gear')


class GearSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
#    category = CategorySerializer(read_only=True)
    #location = LocationSerializer(read_only=True)
    gearproperty_set = GearPropertySerializer(many=True, read_only=True)
    gearavailability_set = GearAvailabilitySerializer(many=True, read_only=True)
    gearimage_set = GearImageSerializer(many=True, read_only=True)
    class Meta:
        model = Gear
        fields = ('id', 'name', 'description', 'brand', 'price', 'expiration_date',
            'preferred_contact', 'payment', 'user', 'category',
            'gearproperty_set', 'gearimage_set', 'gearavailability_set')


class LocationSerializer(serializers.ModelSerializer):
    gear_set = GearSerializer(many=True, read_only=True)
    class Meta:
        model = Location
        geo_field = 'point'
        fields = ('id', 'address', 'point', 'gear_set')
