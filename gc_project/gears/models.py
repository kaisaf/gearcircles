from django.contrib.gis.db import models
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ValidationError
import datetime, os
from users.models import User

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image_storage = FileSystemStorage(location = BASE_DIR + "/static/gears/img")

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
    category = models.ForeignKey(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    address = models.TextField()
    point = models.PointField()
    objects = models.GeoManager()

    def __str__(self):
        return "{} / {}".format(self.address, self.point.coords)


class Gear(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    preferred_contact = models.IntegerField(choices=CONTACT_CHOICES)
    payment = models.IntegerField(choices=PAYMENT_CHOICES)
    expiration_date = models.DateField()
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def check_availability(self, start_date, end_date):
        intersection_dates = GearAvailability.objects.filter(
            not_available_date__gte=start_date
        ).filter(
            not_available_date__lte=end_date
        )
        if len(intersection_dates) > 0:
            return False
        return True

    def __str__(self):
        return self.name

    def clean(self):
        today = datetime.date.today()
        three_months = today + datetime.timedelta(days=90)
        if self.expiration_date > three_months:
            raise ValidationError("Expiration date must be within 90 days.")
        elif today > self.expiration_date:
            raise ValidationError("Expiration date can not be in the past.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super(Gear, self).save(*args, **kwargs)


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
    photo = models.ImageField(storage=image_storage)
    gear = models.ForeignKey(Gear)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "gear:{} photo:{}".format(self.gear, self.photo)
