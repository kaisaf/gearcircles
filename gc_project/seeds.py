import os, sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gc_project.settings")

django.setup()

from gears.models import Category


# categories = ['Avalanche safety', 'Ice climbing/mountaineering', 'Ice axes', 'Crampons',
# 'Ice climbing boots', 'Cross country skiing', 'Other skiing gear', 'Skis', 'Ski boots', 'Other snowboarding gear',
# 'Snowboards', 'Snowboard boots', 'Snowshoeing', 'Camping/hiking', 'Cycling', 'Diving',
# 'Golf', 'Kayaking/Canoeing/Rafting', 'Paddleboarding', 'Rock climbing/Bouldering',
# 'Rollerblading', 'Skateboarding', 'Surfing/Windsurfing/Kitesurfing', 'Wakeboarding/waterskiing',
# 'Sports technology', 'Other winter sports', 'Other summer sports']

gears = ['skis', 'telemark skis', 'snowboard', 'snowboard boots', 'ski boots',
'ski poles', 'trekking poles', 'avalance beacon', 'ABS backbag', 'touring skis',
'touring boots', 'mountaineering ice axe', 'ice axes', 'ice climbing boots',
'ice climbing crampons', 'light crampons', 'tent', 'cooking ware', 'surfboard',
'paddleboard', 'crashpad', 'snowshoes', 'wakeboard', 'cross country skis',
'kayak', 'skiing helmet', 'climbing helmet', 'bicycle helmet', 'bicycle', 'longboard',
'skateboard', 'rollerblades', 'ice skates']

category_properties = ['model', 'size', 'length', 'width']

brands = ['K2', 'Salomon', 'Black Diamond', 'The North Face', 'Beal', 'Gnu', 'Burton',
'Petzl', 'Dynastar', 'LaSportiva', 'Dynafit', 'Grivel', 'Black Crows', 'Scarpa',
'Red', 'Mammuth', 'Sector 9', 'Loaded', 'Giro', 'CAMP', 'Fischer', 'Atomic',
'Quicksilver', 'Rip Curl', 'MSR']

# for category in categories:
#     Category.objects.create(name=category, description="{} description".format(category))


"""
Coordinates:
from faker import faker
from random import randint
from gears.models import Location
from django.contrib.gis.geos import Point, fromstr

fake = Faker()

def create_location():
    lat = fake.geo_coordinate(center=40.7512969, radius=0.1)
    lng = fake.geo_coordinate(center=-73.988602, radius=0.1)
    point = fromstr("POINT({} {})".format(lat, lng)
    address = str[i] + ". location"
    location = Location.objects.create(address=address, point=point)
    return location

def create user():
    name = fake.name()
    email = fake.email()
    score = randint(1, 10)
    phone = fake.phone_number()
    user = User.objects.create(name=name, email=email, score=score, phone=phone)
    return user

def create_gear():
    name = gears[randint(0, len(gears) - 1)]
    description = "test description for " + name
    brand = brands[randint(0, len(brands) - 1)]
    price = randint(1, 75)
    preferred_contact = randint(0, 1)
    payment = randint(0, 2)
    expiration_date =
    categories =
    location = create_location()
    user = create_user()
    Gear.objects.create(name=name, description=description, brand=brand, price=price,
    )













"""
