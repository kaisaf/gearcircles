from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from gears.models import Location

from .gitkit_auth import signin_or_signup_based_on_gitkit

from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.measure import Distance


class IndexView(View):
    def get(self, request):
        co = [39.828175, -98.5795]
        distance_from_point = {'mi':'10000'}
        point = fromstr("POINT({} {})".format(co[0], co[1]))
        center = Location(address="us", point=point)
        locations = Location.objects.filter(point__distance_lte=(center.point, Distance(**distance_from_point) ))
        context = {}
        for location in locations:
            context[location.address] = location.point
        return render(request, "index.html", context)


class LoginView(View):
    def get(self, request):
        print("GET on login")
        return render(request, "users/login.html")


class LogoutView(View):
    def get(self, request):
        return HttpResponse("Hei! LogoutView")


class LoginWidgetView(View):
    def get(self, request):
        print("GET on loginwidget")
        return render(request, "users/loginwidget.html")


class MyAccountView(View):
    def get(self, request):
        return HttpResponse("MyAccount!!!!!")


class HomeView(View):
    def get(self, request):
        print("GET on /home")
        if not request.user.is_authenticated():
            #Should check google cookie and signup/signin user on django
            if not signin_or_signup_based_on_gitkit(request):
                #not signed in on gitkit, redirect to login page
                return redirect(login)
        return HttpResponse("Welcoome to the Login View!")




class UserView(View):
    def get(self, request, user_id):
        return HttpResponse("Userview " + user_id)
