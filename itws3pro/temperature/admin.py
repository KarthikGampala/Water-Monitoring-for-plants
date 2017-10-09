from __future__ import unicode_literals

from django.contrib import admin

from .models import Temperature,Humidity,Moisture,WaterLevel
# Register your models here.
admin.site.register(Temperature)

admin.site.register(Humidity)

admin.site.register(Moisture)

admin.site.register(WaterLevel)
