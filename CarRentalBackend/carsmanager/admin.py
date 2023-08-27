from django.contrib import admin
from carsmanager import models


class CarModel(admin.ModelAdmin):
    list_display = ["name", "model", "price_per_day", "is_available"]


admin.site.register(models.Car, CarModel)
