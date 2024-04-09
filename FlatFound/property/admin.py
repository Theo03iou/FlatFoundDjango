from django.contrib import admin
from .models import Category, Property, Countries

# Register your models here.

admin.site.register(Countries)
admin.site.register(Category)
admin.site.register(Property)

