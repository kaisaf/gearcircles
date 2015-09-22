from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View

from .gitkit_auth import signin_or_signup_based_on_gitkit


class IndexView(View):
    def get(self, request):
        return HttpResponse("Hei! IndexView")
    
    
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
