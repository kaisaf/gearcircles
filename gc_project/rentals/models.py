from django.db import models
from django.core.exceptions import ValidationError

from users.models import User
from gears.models import Gear, GearAvailability

import datetime

import rentals.twilio_helper


PAYMENT_CHOICES = (
    (0, 'Cash'),
    (1, 'Paypal'),
)

class Transaction(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    owner_user = models.ForeignKey(User, related_name="transactions_owned")
    borrower_user = models.ForeignKey(User, related_name="transactions_borrowed")
    price_paid = models.FloatField()
    payment_method = models.IntegerField(choices=PAYMENT_CHOICES)
    gear = models.ForeignKey(Gear)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("End date can not be before start date")
        if not self.gear.check_availability(self.start_date, self.end_date):
            raise ValidationError("Gear not available for given timeframe")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Transaction, self).save(*args, **kwargs)
        for i in range((self.end_date-self.start_date).days + 1):
            not_available = self.start_date + datetime.timedelta(days=i)
            GearAvailability.objects.create(not_available_date=not_available, gear=self.gear)
        twilio_helper.send_sms(
            phone = self.owner_user.phone,
            text = "Your {} just got booked from {} to {}".format(self.gear, self.start_date, self.end_date))
        twilio_helper.send_sms(
            phone = self.borrower_user.phone,
            text = "You just booked a {} from {} to {}".format(self.gear, self.start_date, self.end_date))

    def __str__(self):
        return "gear:{} start_date:{} end_date:{}".format(self.gear, self.start_date, self.end_date)
