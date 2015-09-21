from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

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
