from django.contrib import admin
from . import models


class DriverModel(admin.ModelAdmin):
    list_display = ["first_name", "last_name",
                    "phone_number", 'gender', "age", "is_customer"]


admin.site.register(models.Driver, DriverModel)
