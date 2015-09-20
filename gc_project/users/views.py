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
    def get(self, request, username):
        return HttpResponse("Userview " + username)

class ProductView(View):
    def get(self, request, username, product_id):
        return HttpResponse("Product!!!!! " + username + " " + product_id)
