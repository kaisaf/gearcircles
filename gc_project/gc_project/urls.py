"""gc_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from rest_framework import routers

from users.views import (IndexView, UserViewSet,
                         LogoutView, MyAccountView,
                         LoginWidgetView, UserView)
from gears.views import (HomeView, CategoriesView, CategoryByNameView,
                         GearView, AddGearView, LocationsView,
                         LocationByNameView)
from gears.views import (CategoryViewSet, CategoryPropertyViewSet,
                        GearViewSet, GearPropertyViewSet,
                        GearAvailabilityViewSet, GearImageViewSet,
                        LocationViewSet)

from rentals.views import TransactionViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'gears', GearViewSet)
router.register(r'gearproperties', GearPropertyViewSet)
router.register(r'gearavailabilities', GearAvailabilityViewSet)
router.register(r'gearimages', GearImageViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^loginwidget/', LoginWidgetView.as_view(), name='loginwidget'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^home/', login_required(HomeView.as_view()), name='home'),
    url(r'^myaccount/', MyAccountView.as_view(), name='myaccount'),
    url(r'^users/(?P<user_id>\w+)/$', UserView.as_view(), name='user'),
    url(r'^gears/(?P<gear_id>\w+)/$', GearView.as_view(), name='gear'),
    url(r'^addgear/', AddGearView.as_view(), name='addgear'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
]
