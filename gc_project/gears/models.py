from django.db import models
from django.core.exceptions import ValidationError
import datetime
from users.models import User


PAYMENT_CHOICES = (
    (0, 'Cash'),
    (1, 'Paypal'),
    (2, 'Any')
)

CONTACT_CHOICES = (
    (0, 'Phone'),
    (1, 'Email'),
)

INPUT_CHOICES = (
    (0, 'String'),
    (1, 'Integer'),
    (2, 'Float'),
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CategoryProperty(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    mandatory = models.BooleanField()
    input_type = models.IntegerField(choices=INPUT_CHOICES)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Gear(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    preferred_contact = models.IntegerField(choices=CONTACT_CHOICES)
    payment = models.IntegerField(choices=PAYMENT_CHOICES)
    expiration_date = models.DateField()
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def clean(self):
        today = datetime.date.today()
        three_months = today + datetime.timedelta(days=90)
        if self.expiration_date > three_months:
            raise ValidationError("Expiration date must be within 90 days.")
        elif today > self.expiration_date:
            raise ValidationError("Expiration date can not be in the past.")


class GearProperty(models.Model):
    value = models.CharField(max_length=50)
    gear = models.ForeignKey(Gear)
    category_property = models.ForeignKey(CategoryProperty)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "gear:{} value:{}".format(self.gear, self.value)


class GearAvailability(models.Model):
    not_available_date = models.DateField()
    gear = models.ForeignKey(Gear)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "gear:{} not_available_date:{}".format(self.gear, self.not_available_date)


class GearImage(models.Model):
    photo = models.ImageField()
    gear = models.ForeignKey(Gear)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "gear:{} photo:{}".format(self.gear, self.photo)
