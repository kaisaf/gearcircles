from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

class LoginView(View):
    def get(self, request):
        return HttpResponse("MOI! LoginView")

class LogoutView(View):
    def get(self, request):
        return HttpResponse("Hei! LogoutView")

class LoginWidgetView(View):
    def get(self, request):
        return HttpResponse("MOI! LoginwidgetView")

class MyAccountView(View):
    def get(self, request):
        return HttpResponse("MyAccount!!!!!")

class UserView(View):
    def get(self, request, user_id):
        return HttpResponse("Userview " + user_id)
