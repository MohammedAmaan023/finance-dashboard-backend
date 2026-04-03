from django.contrib import admin
from .models import User, Record
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("role",)}),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(Record)