from rest_framework import serializers
from .models import Category, CategoryProperty, Gear, GearProperty, Location, GearAvailability, GearImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class CategoryPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProperty
        fields = ('name', 'description', 'mandatory', 'input_type', 'categories')


class GearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gear
        fields = ('name', 'description', 'brand', 'price', 'expiration_date', 'user',
            'location', 'categories', 'preferred_contact', 'payment')


class GearPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = GearProperty
        fields = ('value', 'gear', 'category_property')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('address', 'point')


class GearAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = GearAvailability
        fields = ('not_available_date', 'gear')


class GearImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GearImage
        fields = ('photo', 'gear')
