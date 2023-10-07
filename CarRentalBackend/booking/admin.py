from django.contrib import admin
from . import models


class BookModel(admin.ModelAdmin):
    list_display = ["customer", "booked_car",
                    "pick_up_date", "return_date", "status"]


# Register your models here.
admin.site.register(models.Booking, BookModel)
admin.site.register(models.Agreement)
