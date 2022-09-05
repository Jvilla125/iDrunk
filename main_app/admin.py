from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Drink, CustomUser
# Register your models here.

admin.site.register(Drink)
admin.site.register(CustomUser)

class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = 'customUser'

class UserAdmin(BaseUserAdmin):
    inlines = (CustomUserInline,)
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)