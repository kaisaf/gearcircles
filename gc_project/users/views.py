from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import logout

from gears.models import Location, Gear
from .models import User
from rentals.models import Transaction
from .serializers import UserSerializer

from .gitkit_auth import signin_or_signup_based_on_gitkit

from rest_framework import viewsets

from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.measure import Distance


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated():
            # user already logged in, redirect to Home
            return redirect("home")

        if signin_or_signup_based_on_gitkit(request):
            # check if user is logged in on gitkit, signup/sigin on django and redurect to Home
            return redirect("home")

        return render(request, "index.html")
#        co = [39.828175, -98.5795]
#        distance_from_point = {'mi':'10000'}
#        point = fromstr("POINT({} {})".format(co[0], co[1]))
#        center = Location(address="us", point=point)
#        locations = Location.objects.filter(point__distance_lte=(center.point, Distance(**distance_from_point) ))
#        context = {}
#        for location in locations:
#            context[location.address] = location.point


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")


class LoginWidgetView(View):
    def get(self, request):
        print("GET on loginwidget")
        return render(request, "users/loginwidget.html")


class MyAccountView(View):
    def get(self, request):
        gears_i_rented = Transaction.objects.filter(borrower_user=request.user)
        my_gears_rented = Transaction.objects.filter(owner_user=request.user)
        my_gears = Gear.objects.filter(user=request.user)
        print('gears i rented: {}'.format(gears_i_rented))
        print('my gears rented: {}'.format(my_gears_rented))
        print('my gears: {}'.format(my_gears))
        return render(request, 'users/myaccount.html')


class UserView(View):
    def get(self, request, user_id):
        return HttpResponse("Userview " + user_id)


class UserViewSet(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class = UserSerializer
