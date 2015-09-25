import os, sys
import django

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gc_project.settings")

django.setup()

from gears.models import Category


categories = ['Avalanche safety', 'Ice climbing/mountaineering', 'Ice axes', 'Crampons',
'Ice climbing boots', 'Cross country skiing', 'Other skiing gear', 'Skis', 'Ski boots', 'Other snowboarding gear',
'Snowboards', 'Snowboard boots', 'Snowshoeing', 'Camping/hiking', 'Cycling', 'Diving',
'Golf', 'Kayaking/Canoeing/Rafting', 'Paddleboarding', 'Rock climbing/Bouldering',
'Rollerblading', 'Skateboarding', 'Surfing/Windsurfing/Kitesurfing', 'Wakeboarding/waterskiing',
'Sports technology', 'Other winter sports', 'Other summer sports']

gears = ['skis', 'telemark skis', 'snowboard', 'snowboard boots', 'ski boots',
'ski poles', 'trekking poles', 'avalance beacon', 'ABS backbag', 'touring skis',
'touring boots', 'mountaineering ice axe', 'ice axes', 'ice climbing boots',
'ice climbing crampons', 'light crampons', 'tent', 'cooking ware', 'surfboard',
'paddleboard', 'crashpad', 'snowshoes', 'wakeboard', 'cross country skis',
'kayak', 'skiing helmet', 'climbing helmet', 'bicycle helmet', 'bicycle', 'longboard',
'skateboard', 'rollerblades', 'ice skates']

category_properties = ['model', 'size', 'length', 'width']

for category in categories:
    Category.objects.create(name=category, description="{} description".format(category))
