from django.db import models
from users.models import User
from gears.models import Gear, GearAvailability
import datetime


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

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)
        for i in range((self.end_date-self.start_date).days + 1):
            not_available = self.start_date + datetime.timedelta(days=i)
            GearAvailability.objects.create(not_available_date=not_available, gear=self.gear)

    def __str__(self):
        return "gear:{} start_date:{} end_date:{}".format(self.gear, self.start_date, self.end_date)
