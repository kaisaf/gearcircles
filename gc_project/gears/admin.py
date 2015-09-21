from django.contrib import admin
from .models import Category, CategoryProperty, Gear, GearProperty, GearAvailability


admin.site.register(Category)
admin.site.register(CategoryProperty)
admin.site.register(Gear)
admin.site.register(GearProperty)
admin.site.register(GearAvailability)
