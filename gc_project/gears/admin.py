from django.contrib import admin
from .models import Category, CategoryProperty, Gear, GearProperty, GearAvailability


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
