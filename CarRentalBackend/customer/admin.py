from django.contrib import admin
from . import models


class CustomerModel(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone_number", "age"]


admin.site.register(models.Customer, CustomerModel)
