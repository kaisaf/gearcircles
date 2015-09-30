import os, sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gc_project.settings")
django.setup()

from gears.models import Category, CategoryProperty, Location, Gear, GearProperty, GearAvailability, GearImage
from users.models import User

Category.objects.all().delete()
Gear.objects.all().delete()
User.objects.all().delete()
CategoryProperty.objects.all().delete()
GearProperty.objects.all().delete()
Location.objects.all().delete()

## SKIS ####
skis = Category.objects.create(
    name="Skis",
    description="Skis",
    )

skis_model = CategoryProperty.objects.create(
    name = "model",
    description = "Gotama, Bonafide, etc",
    mandatory = False,
    input_type = 0, # string
    category = skis,
    )

skis_binding = CategoryProperty.objects.create(
    name = "binding",
    description = "Look PX12, Marker Griffon, Rossignol Axial3 etc",
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
    description = "Camber, Rocker, Tip Rocker, etc",
    mandatory = False,
    input_type = 0,
    category = skis,
    )

skis_style = CategoryProperty.objects.create(
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
#
#### SKI BOOTS ####
skiBoots = Category.objects.create(
    name= "Ski Boots",
    description= "Ski boots",
    )

skiBoots_model = CategoryProperty.objects.create(
    name = "model",
    description = "SX120, T1, Krypton Pro ID, etc",
    mandatory = True,
    input_type = 0, # string
    category = skiBoots,
    )

skiBoots_size = CategoryProperty.objects.create(
    name = "size",
    description = "24.5, 30.0 etc",
    mandatory = True,
    input_type = 2,
    category = skiBoots,
    )

skiBoots_style = CategoryProperty.objects.create(
    name = "style",
    description = "Alpine, Telemark, Touring, etc",
    mandatory = True,
    input_type = 0,
    category = skiBoots,
)

skiBoots_level = CategoryProperty.objects.create(
    name = "level",
    description = "Beginner, Intermediate, Advanced, Expert",
    mandatory = False,
    input_type = 0,
    category = skiBoots,
    )

#### SNOWBOARDS ####
snowboards = Category.objects.create(
    name= "Snowboards",
    description= "Snowboards",
    )

snowboards_model = CategoryProperty.objects.create(
    name = "model",
    description = "Gateway, Custom Fly V, Smart Pickle, etc",
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
    description = "Park, Freeride, All-Mountain, Powder, etc",
    mandatory = False,
    input_type = 0,
    category = snowboards,
    )


#### SNOWBOARD BOOTS ####
snowboardsBoots = Category.objects.create(
    name= "Snowboard Boots",
    description= "Snowboards Boots",
    )

snowboardsBoots_model = CategoryProperty.objects.create(
    name = "model",
    description = "Ion LTD, Moto, Encore, etc",
    mandatory = False,
    input_type = 0, # string
    category = snowboardsBoots,
    )

snowboardsBoots_size = CategoryProperty.objects.create(
    name = "size",
    description = "7, 9.5, 12, etc",
    mandatory = True,
    input_type = 2,
    category = snowboardsBoots,
    )

snowboardsBoots_flex = CategoryProperty.objects.create(
    name = "flex",
    description = "Soft, Medium, Stiff, etc",
    mandatory = False,
    input_type = 0,
    category = snowboardsBoots,
    )


#### ROLLERBLADING ####
rollerblading = Category.objects.create(
    name= "Rollerblading",
    description= "Rollerblading/Inline Skating",
    )

rollerblading_model = CategoryProperty.objects.create(
    name = "model",
    description = "Farmer 5, Carbon 3, TV3, etc",
    mandatory = False,
    input_type = 0, # string
    category = rollerblading,
    )

rollerblading_size = CategoryProperty.objects.create(
    name = "size",
    description = "7, 9.5, 12, etc",
    mandatory = True,
    input_type = 2,
    category = rollerblading,
    )

rollerblading_style = CategoryProperty.objects.create(
    name = "style",
    description = "Vert, Street, Powerblade, Fitness, etc",
    mandatory = False,
    input_type = 0,
    category = rollerblading,
    )


#### CYCLING ####
cycling = Category.objects.create(
    name= "Cycling",
    description= "Cycling/Mountain Biking",
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
    description = "Dutch, Road, Fixed, Mountain Bike, Cruizer, etc",
    mandatory = False,
    input_type = 0,
    category = cycling,
    )


#### ICE AXES ####
iceAxes = Category.objects.create(
    name="Ice Axes",
    description="Ice climbing/mountaineering axes",
    )

iceAxes_model = CategoryProperty.objects.create(
    name = "model",
    description = "Raven, Viper, Quark, etc",
    mandatory = False,
    input_type = 0, # string
    category = iceAxes,
    )

iceAxes_style = CategoryProperty.objects.create(
    name = "style",
    description = "Mountaineering, Ice Climbing",
    mandatory = False,
    input_type = 0,
    category = iceAxes,
    )


#### CRAMPONS ####
crampons = Category.objects.create(
    name="Crampons",
    description="Ice climbing/mountaineering crampons",
    )

crampons_model = CategoryProperty.objects.create(
    name = "model",
    description = "Cyborg Pro, G14, Vasak, etc",
    mandatory = False,
    input_type = 0, # string
    category = crampons,
    )

crampons_style = CategoryProperty.objects.create(
    name = "style",
    description = "Mountaineering, Ice Climbing, Race",
    mandatory = False,
    input_type = 0,
    category = crampons,
    )

crampons_style = CategoryProperty.objects.create(
    name = "style",
    description = "Mountaineering, Ice Climbing, Race, Snow Walking",
    mandatory = False,
    input_type = 0,
    category = crampons,
    )

crampons_binding = CategoryProperty.objects.create(
    name = "binding",
    description = "Step-In, Strap-On, Hybrid",
    mandatory = False,
    input_type = 0,
    category = crampons,
    )


#### ICE CLIMBING BOOTS ####
iceBoots = Category.objects.create(
    name="Ice Climbing Boots",
    description="Ice climbing/mountaineering boots, no hiking boots",
    )

iceBoots_model = CategoryProperty.objects.create(
    name = "model",
    description = "Cyborg Pro, G14, Vasak, etc",
    mandatory = False,
    input_type = 0, # string
    category = iceBoots,
    )

iceBoots_size = CategoryProperty.objects.create(
    name = "size",
    description = "7, 9.5, 12, etc",
    mandatory = True,
    input_type = 2,
    category = iceBoots,
    )


#### GEAR VARIABLES ####

skis_names = ['skis', 'telemark skis', 'touring skis']
skis_brands = ['K2', 'Salomon', 'Black Diamond', 'Dynastar', 'Dynafit', 'Black Crows', 'Fischer', 'Atomic']

skiboots_names = ['touring boots', 'ski boots', 'telemark boots']
skiboots_brands = ['K2', 'Salomon', 'Black Diamond', 'Dynafit', 'Scarpa', 'Atomic', 'Nordica']

snowboards_names = ['snowboard', 'splitboard']
snowboards_brands = ['GNU', 'Burton', 'Lib Tech', 'Ride', 'Arbor']

snowboardBoots_names = ['snowboard boots']
snowboardBoots_brands = ['Burton', 'Salomon', 'K2', 'ThirtyTwo']

iceAxes_names = ['mountaineering ice axe', 'ice axes']
iceAxes_brands = ['Petzl', 'Black Diamond', 'Simond', 'CAMP']

crampons_names = ['ice climbing crampons', 'light crampons']
crampons_brands = ['Grivel', 'Petzl', 'Black Diamond', 'Simond', 'CAMP']

iceBoots_names = ['ice climbing boots']
iceBoots_brands = ['Scarpa', 'LaSportiva', 'Asolo', 'Millet']

cycling_names = ['mountain bike', 'hybrid bicycle', 'fixie']
cycling_brands = ['Trek', 'Giant', 'Cannondale', 'Bianchi']

rollerblading_names = ['inline skates', 'rollerblades']
rollerblading_brands = ['K2', 'Roces', 'Rollerblade']



import datetime
from faker import Faker
from random import randint
from gears.models import Location
from users.models import User
from django.contrib.gis.geos import Point, fromstr

fake = Faker()

#### GEAR PROPERTY SEEDS ####
skiBoots_sizes = [23.5, 24, 24.5, 25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30]
boot_sizes = [5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12]

skis_length = randint(145, 198)
skis_width = [79, 80, 81, 82, 84, 88, 90, 92, 95, 96, 98, 101, 103, 105, 108, 110, 115, 120, 125]

snowboard_length = randint(140, 170)


### CREATE USERS ####
def create_user():
    name = fake.name()
    email = fake.email()
    score = randint(1, 10)
    phone = fake.phone_number()
    phone = phone[:14]
    user = User.objects.create(name=name, email=email, score=score, phone=phone)
    return user

for i in range (1, 1000):
    create_user()



#### CREATE LOCATION ####
def create_location(name):
    lat = fake.geo_coordinate(center=40.7509862, radius=0.5)
    lng = fake.geo_coordinate(center=-73.986871, radius=0.5)
    point = fromstr("POINT({} {})".format(lng, lat))
    address = name + " location"
    location = Location.objects.create(address=address, point=point)
    return location


### CREATE GEAR ####
def create_gear(names, brands, user):
    name = names[randint(0, len(names)-1)]
    description = "test description for " + name
    brand = brands[randint(0, len(brands)-1)]
    price = randint(1, 75)
    preferred_contact = randint(0, 1)
    payment = randint(0, 2)
    days_for_exp = randint(1, 90)
    expiration_date = datetime.date.today() + datetime.timedelta(days=days_for_exp)
    location = create_location(name)
    user = user
    new_gear = Gear.objects.create(name=name, description=description, brand=brand, price=price,
        preferred_contact=preferred_contact, payment=payment, expiration_date=expiration_date,
        location=location, user=user)
    return new_gear

users = User.objects.all()

for i in range(0, 500):
    user = users[randint(0, len(users)-1)]
    a = randint(1, 9)
    if a == 1:
        category_name = "Skis"
        category = Category.objects.get(name="Skis")
        photo = "./skis.jpg"
        new_gear = create_gear(skis_names, skis_brands, user)
        cat_prop = CategoryProperty.objects.get(name="length", category=category)
        gear_property1 = GearProperty.objects.create(value=randint(145, 198), gear=new_gear, category_property=cat_prop)
    elif a == 2:
        category_name = "Ski Boots"
        photo = "./ski_boots.jpg"
        new_gear = create_gear(skiboots_names, skiboots_brands, user)
        # cat_prop = CategoryProperty.objects.get(name="size")
        # gear_property1 = GearProperty.objects.create(value=skiBoots_sizes[randint(0, len(skiBoots_sizes)-1)], gear=new_gear, category_property=cat_prop)
    elif a == 3:
        category_name = "Snowboards"
        photo = "./snowboard.jpg"
        new_gear = create_gear(snowboards_names, snowboards_brands, user)
        # cat_prop = CategoryProperty.objects.get(name="length")
        # gear_property1 = GearProperty.objects.create(value=randint(140, 170), gear=new_gear, category_property=cat_prop)
    elif a == 4:
        category_name = "Snowboard Boots"
        photo = "./snowboard_boots.jpg"
        new_gear = create_gear(snowboardBoots_names, snowboardBoots_brands, user)
        # cat_prop = CategoryProperty.objects.get(name="size")
        # gear_property1 = GearProperty.objects.create(value=boot_sizes[randint(0, len(boot_sizes)-1)], gear=new_gear, category_property=cat_prop)
    elif a == 5:
        category_name = "Ice Axes"
        photo = "./ice_axes.jpg"
        new_gear = create_gear(iceAxes_names, iceAxes_brands, user)
        # cat_prop = CategoryProperty.objects.get(name="model")
        # gear_property1 = GearProperty.objects.create(value="Cobra", gear=new_gear, category_property=cat_prop)
    elif a == 6:
        category_name = "Crampons"
        photo = "./crampons.jpg"
        new_gear = create_gear(crampons_names, crampons_brands, user)
        # cat_prop = CategoryProperty.objects.get(name="binding")
        # gear_property1 = GearProperty.objects.create(value="Step-In", gear=new_gear, category_property=cat_prop)
    elif a == 7:
        category_name = "Ice Climbing Boots"
        photo = "./ice_boots.jpg"
        new_gear = create_gear(iceBoots_names, iceBoots_brands, user)
        # cat_prop = CategoryProperty.objects.get(name="size")
        # gear_property1 = GearProperty.objects.create(value=boot_sizes[randint(0, len(boot_sizes)-1)], gear=new_gear, category_property=cat_prop)
    elif a == 8:
        category_name = "Cycling"
        photo = "./bicycle.jpg"
        new_gear = create_gear(cycling_names, cycling_brands, user)
        # cat_prop = CategoryProperty.objects.get(name="frame size")
        # gear_property1 = GearProperty.objects.create(value="Medium", gear=new_gear, category_property=cat_prop)
    elif a == 9:
        category_name = "Rollerblading"
        photo = "./rollerblades.jpg"
        new_gear = create_gear(rollerblading_names, rollerblading_brands, user)
        # cat_prop = CategoryProperty.objects.get(name="size")
        # gear_property1 = GearProperty.objects.create(value=boot_sizes[randint(0, len(boot_sizes)-1)], gear=new_gear, category_property=cat_prop)

    new_gear_category = Category.objects.get(name=category_name)
    new_gear.categories = (new_gear_category,)

    new_image = GearImage.objects.create(photo=photo, gear=new_gear)






categories = ['Avalanche safety', 'Other ice climbing/mountaineering gear',
'Cross country skiing', 'Other skiing gear', 'Other snowboarding gear', 'Snowshoeing', 'Camping/hiking', 'Diving',
'Golf', 'Kayaking/Canoeing/Rafting', 'Paddleboarding', 'Rock climbing/Bouldering',
'Skateboarding', 'Surfing/Windsurfing/Kitesurfing', 'Wakeboarding/waterskiing',
'Sports technology', 'Other winter sports', 'Other summer sports']


gears = ['ski poles', 'trekking poles', 'avalance beacon', 'ABS backbag',
'tent', 'cooking ware', 'surfboard', 'paddleboard', 'crashpad', 'snowshoes', 'wakeboard',
'cross country skis', 'kayak', 'skiing helmet', 'climbing helmet', 'bicycle helmet',
'bicycle', 'longboard', 'skateboard', 'rollerblades', 'ice skates']
