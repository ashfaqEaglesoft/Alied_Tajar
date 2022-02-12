from importlib.metadata import distributions
from django.contrib import admin

from .models import Area, Country, Distric, Personal,Business, Province, Tehsil

# Register your models here.

admin.site.register(Personal)
admin.site.register(Business)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(Distric)
admin.site.register(Tehsil)
admin.site.register(Area)
