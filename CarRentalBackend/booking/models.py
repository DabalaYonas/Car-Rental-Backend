from django.db import models
from carsmanager.models import Car
from driver.models import Driver

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
    booked_driver = models.ForeignKey(
        Driver, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(
        max_length=200, choices=STATUS, default=PEND, null=True, blank=True)

    def __str__(self):
        return str(self.pick_up_date)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.booked_car.is_available = False
        self.booked_car.save()
        print("Booked car", self.booked_car)
