from django.contrib import admin
from carsmanager import models


class CarModel(admin.ModelAdmin):
    list_display = ["name", "model_year", "price_per_day",
                    "with_driver", "is_available"]


admin.site.register(models.Car, CarModel)
