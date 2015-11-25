from django.contrib.gis import admin
from .models import Category, CategoryProperty, Location, Gear, GearProperty, GearAvailability, GearImage


class CategoryPropertyInline(admin.StackedInline):
    model = CategoryProperty
    extra = 1


class GearPropertyInline(admin.TabularInline):
    model = GearProperty
    extra = 1


class GearAvailabilityInline(admin.StackedInline):
    model = GearAvailability
    extra = 1


class GearImageInline(admin.StackedInline):
    model = GearImage
    extra = 1


class LocationInline(admin.StackedInline):
    model = Location
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display =  ('name', 'description')
    search_fields = ['name']
    inlines = [CategoryPropertyInline]


class CategoryPropertyAdmin(admin.ModelAdmin):
    list_display =  ('name', 'category', 'description')


class GearAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'user', 'price', 'location')
    search_fields = ['name']
    list_filter = ['category']
    inlines = [GearPropertyInline, GearAvailabilityInline, GearImageInline]


class GearPropertyAdmin(admin.ModelAdmin):
    list_display =  ('value', 'gear')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Gear, GearAdmin)
admin.site.register(Location)
