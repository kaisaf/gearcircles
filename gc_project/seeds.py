import os, sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gc_project.settings")

django.setup()

from gears.models import Category, CategoryProperty, Location, Gear, GearProperty, GearAvailability, GearImage

Category.objects.all().delete()

#### SKIS ####
skis = Category.objects.create(
    name="Skis",
    description="Skis",
    )

skis_model = CategoryProperty.objects.create(
    name = "model",
    description = "Gotama, Bonafide, etc...",
    mandatory = False,
    input_type = 0, # string
    category = skis,
    )

skis_length = CategoryProperty.objects.create(
    name = "length",
    description = "187, 144, etc",
    mandatory = False,
    input_type = 1,
    category = skis,
    )

skis_width = CategoryProperty.objects.create(
    name = "width",
    description = "125.0, 108.5, etc",
    mandatory = False,
    input_type = 2,
    category = skis,
    )

skis_profile = CategoryProperty.objects.create(
    name = "profile",
    description = "Camber, Rocker, etc",
    mandatory = False,
    input_type = 0,
    category = skis,
    )

skis_style = CategoryProperty.objecs.create(
    name = "style",
    description = "Alpine, Telemark, Touring, etc",
    mandatory = True,
    input_type = 0,
    category = skis,
)

skis_level = CategoryProperty.objects.create(
    name = "level",
    description = "Beginner, Intermediate, Advanced, Expert",
    mandatory = False,
    input_type = 0,
    category = skis,
    )

#### SNOWBOARDS ####
snowboards = Category.objects.create(
    name="Snowboards",
    description="Snowboards",
    )

snowboards_model = CategoryProperty.objects.create(
    name = "model",
    description = "Gateway, Custom Fly V, Smart Pickle, etc...",
    mandatory = False,
    input_type = 0, # string
    category = snowboards,
    )

snowboards_size = CategoryProperty.objects.create(
    name = "size",
    description = "139, 152, 164, etc",
    mandatory = False,
    input_type = 1,
    category = snowboards,
    )

snowboards_width = CategoryProperty.objects.create(
    name = "width",
    description = "Regular, Wide, etc",
    mandatory = False,
    input_type = 0,
    category = snowboards,
    )

snowboards_profile = CategoryProperty.objects.create(
    name = "profile",
    description = "Camber, Rocker, etc",
    mandatory = False,
    input_type = 0,
    category = snowboards,
    )

snowboards_level = CategoryProperty.objects.create(
    name = "level",
    description = "Beginner, Intermediate, Advanced, Expert",
    mandatory = True,
    input_type = 0,
    category = snowboards,
    )

snowboards_terrain = CategoryProperty.objects.create(
    name = "terrain",
    description = "Park, Freeride, All-Mountain, Powder, etc...",
    mandatory = False,
    input_type = 0,
    category = snowboards,
    )


#### SNOWBOARD BOOTS ####
snowboardsBoots = Category.objects.create(
    name="Snowboards Boots",
    description="Snowboards Boots",
    )

snowboardsBoots_model = CategoryProperty.objects.create(
    name = "model",
    description = "Ion LTD, Moto, Encore, etc...",
    mandatory = False,
    input_type = 0, # string
    category = snowboardsBoots,
    )

snowboardsBoots_size = CategoryProperty.objects.create(
    name = "size",
    description = "7, 9.5, 12, etc...",
    mandatory = True,
    input_type = 2,
    category = snowboardsBoots,
    )

snowboardsBoots_flex = CategoryProperty.objects.create(
    name = "width",
    description = "Soft, Medium, Stiff, etc...",
    mandatory = False,
    input_type = 0,
    category = snowboardsBoots,
    )


#### ROLLERBLADING ####
rollerblading = Category.objects.create(
    name="rollerblading",
    description="Rollerblading/Inline Skating",
    )

rollerblading_model = CategoryProperty.objects.create(
    name = "model",
    description = "Farmer 5, Carbon 3, TV3, etc...",
    mandatory = False,
    input_type = 0, # string
    category = rollerblading,
    )

rollerblading_size = CategoryProperty.objects.create(
    name = "size",
    description = "7, 9.5, 12, etc...",
    mandatory = True,
    input_type = 2,
    category = rollerblading,
    )

rollerblading_style = CategoryProperty.objects.create(
    name = "style",
    description = "Vert, Street, Powerblade, Fitness, etc...",
    mandatory = False,
    input_type = 0,
    category = rollerblading,
    )


#### CYCLING ####
cycling = Category.objects.create(
    name="cycling",
    description="Cycling/Mountain Biking",
    )

cycling_model = CategoryProperty.objects.create(
    name = "model",
    description = "Cycling, Mountain Biking, etc",
    mandatory = False,
    input_type = 0, # string
    category = cycling,
    )

cycling_size = CategoryProperty.objects.create(
    name = "frame size",
    description = "Small, Medium, Large",
    mandatory = False,
    input_type = 2,
    category = cycling,
    )

cycling_style = CategoryProperty.objects.create(
    name = "style",
    description = "Dutch, Road, Fixed, Mountain Bike, Cruizer, etc...",
    mandatory = False,
    input_type = 0,
    category = cycling,
    )





categories = ['Avalanche safety', 'Ice climbing/mountaineering', 'Ice axes', 'Crampons',
'Ice climbing boots', 'Cross country skiing', 'Other skiing gear', 'Ski boots', 'Other snowboarding gear', 'Snowshoeing', 'Camping/hiking', 'Diving',
'Golf', 'Kayaking/Canoeing/Rafting', 'Paddleboarding', 'Rock climbing/Bouldering',
'Skateboarding', 'Surfing/Windsurfing/Kitesurfing', 'Wakeboarding/waterskiing',
'Sports technology', 'Other winter sports', 'Other summer sports']


gears = ['skis', 'telemark skis', 'snowboard', 'snowboard boots', 'ski boots',
'ski poles', 'trekking poles', 'avalance beacon', 'ABS backbag', 'touring skis',
'touring boots', 'mountaineering ice axe', 'ice axes', 'ice climbing boots',
'ice climbing crampons', 'light crampons', 'tent', 'cooking ware', 'surfboard',
'paddleboard', 'crashpad', 'snowshoes', 'wakeboard', 'cross country skis',
'kayak', 'skiing helmet', 'climbing helmet', 'bicycle helmet', 'bicycle', 'longboard',
'skateboard', 'rollerblades', 'ice skates']


brands = ['K2', 'Salomon', 'Black Diamond', 'The North Face', 'Beal', 'Gnu', 'Burton',
'Petzl', 'Dynastar', 'LaSportiva', 'Dynafit', 'Grivel', 'Black Crows', 'Scarpa',
'Red', 'Mammuth', 'Sector 9', 'Loaded', 'Giro', 'CAMP', 'Fischer', 'Atomic',
'Quicksilver', 'Rip Curl', 'MSR']


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
