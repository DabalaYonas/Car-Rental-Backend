from django.db import models
from carsmanager.models import Car
from customer.models import Customer

ACC = "ACCEPTED"
CANC = "CANCELLED"
PEND = "PENDING"
RET = "RETURNED"

STATUS = ((ACC, "ACCEPTED"),
          (PEND, "PENDING"),
          (CANC, "CANCELLED"),
          (RET, "RETURNED"),
          )


class Booking(models.Model):
    pick_up_date = models.DateField()
    return_date = models.DateField()

    booked_car = models.ForeignKey(
        Car, on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=200, choices=STATUS, default=PEND, null=True, blank=True)

    def __str__(self):
        return str(self.pick_up_date)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == PEND or self.status == ACC:
            self.booked_car.is_available = False
            self.booked_car.save()


def uploaded_to(int, filename):
    return ("images/signature/" + filename)

class Agreement(models.Model):
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, null=True, blank=True)
    
    date = models.DateField(auto_now=True, null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)

    signature = models.ImageField(
        upload_to=uploaded_to, width_field="width_length", height_field="heigth_length", null=True, blank=True)
    width_length = models.IntegerField(default=0, null=True, blank=True)
    heigth_length = models.IntegerField(default=0, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
