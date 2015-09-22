from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .payment import paypal_payment

# Should this be product view? In that case just move it from users

# def ProductView(View):
#     def get(self, request):
#         return HttpResponse("ProductView")
#     def post(self, request):
#         recipient_email =
#         days_rented =
#         dollars = days_rented * <dollars per day>
#         cancel_return_address = <this is the current address>
#         paypal_redirect_address = paypal_payment(recipient_email, dollars, cancel_return_address)
#         return redirect(paypal_redirect_address)
