from django.db import models
from users.models import User


PAYMENT_CHOICES = (
    (0, 'Cash'),
    (1, 'Paypal'),
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


class CategoryProperty(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    mandatory = models.BooleanField()
    input_type = models.IntegerField(choices=INPUT_CHOICES)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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


class GearProperty(models.Model):
    value = models.CharField(max_length=50)
    gear = models.ForeignKey(Gear)
    category_property = models.ForeignKey(CategoryProperty)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GearAvailability(models.Model):
    not_available_date = models.DateField()
    gear = models.ForeignKey(Gear)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GearImage(models.Model):
    photo = models.ImageField()
    gear = models.ForeignKey(Gear)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
