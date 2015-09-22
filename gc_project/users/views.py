from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class IndexView(View):
    def get(self, request):
        return HttpResponse("Hei! IndexView")
    
    
class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")
    
    
class LogoutView(View):
    def get(self, request):
        return HttpResponse("Hei! LogoutView")
    
    
class LoginWidgetView(View):
    def get(self, request):
        return render(request, "users/loginwidget.html")
    
    
class MyAccountView(View):
    def get(self, request):
        return HttpResponse("MyAccount!!!!!")
    
    
class HomeView(View):
    def get(self, request):
        return HttpResponse("Home!!!!!")
    
    
class UserView(View):
    def get(self, request, user_id):
        return HttpResponse("Userview " + user_id)
