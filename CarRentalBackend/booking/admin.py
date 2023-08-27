from django.contrib import admin
from . import models


class BookModel(admin.ModelAdmin):
    list_display = ["booked_driver", "booked_car",
                    "pick_up_date", "return_date", "status"]


class DriverModel(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "age"]


# Register your models here.
admin.site.register(models.Booking, BookModel)
admin.site.register(models.Driver, DriverModel)
