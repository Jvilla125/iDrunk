from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Drink, Photo, Review

admin.site.register(Drink)
admin.site.register(Photo)
admin.site.register(Review)


