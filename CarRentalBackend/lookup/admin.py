from django.contrib import admin
from . import models

admin.site.register(models.Car_Brand)
admin.site.register(models.Car_Categories)
admin.site.register(models.Car_Engines)
admin.site.register(models.Car_Transmission)