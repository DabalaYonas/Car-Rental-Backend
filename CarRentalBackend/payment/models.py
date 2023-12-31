from django.db import models
from booking.models import Booking
import datetime


TELEBIRR = "TELEBIRR"
CBE = "CBE"
CHAPA = "CHAPA"

PAYMENT_METHODS = ((TELEBIRR, "TELEBIRR"),
                   (CBE, "CBE"),
                   (CHAPA, "CHAPA"))


PAID = "PAID"
NOT_PAID = "NOT PAID"
PEND = "PENDING"

PAYMENT_STATUS = ((PAID, "PAID"),
                  (NOT_PAID, "NOT PAID"),
                  (PEND, "PENDING"))


class Payment(models.Model):
    amount = models.IntegerField()
    method = models.CharField(max_length=200, choices=PAYMENT_METHODS)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    tnx_id = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(
        max_length=200, choices=PAYMENT_STATUS, default=NOT_PAID)
    description = models.CharField(max_length=200, null=True, blank=True)
    paid_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.paid_date = datetime.date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.amount)
