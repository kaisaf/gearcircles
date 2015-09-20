from django.db import models
from users.models import User
from gears.models import Gear


class Transaction(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    owner_user = models.ForeignKey(User, related_name="transactions_owned")
    borrower_user = models.ForeignKey(User, related_name="transactions_borrowed")
    price_paid = models.FloatField()
    payment_method = models.IntegerField()
    gear = models.ForeignKey(Gear)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
