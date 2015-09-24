from django.contrib.gis import admin
from .models import Category, CategoryProperty, Location, Gear, GearProperty, GearAvailability, GearImage


class CategoryPropertyInline(admin.StackedInline):
    model = CategoryProperty.categories.through
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryPropertyInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryProperty)
admin.site.register(Gear)
admin.site.register(GearProperty)
admin.site.register(GearAvailability)
admin.site.register(Location)
admin.site.register(GearImage)
