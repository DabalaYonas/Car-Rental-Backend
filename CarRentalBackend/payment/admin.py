from django.contrib import admin
from . import models


class PaymentModel(admin.ModelAdmin):
    list_display = ["amount", "booking", "tnx_id", "method", "status"]


# Register your models here.
admin.site.register(models.Payment, PaymentModel)
