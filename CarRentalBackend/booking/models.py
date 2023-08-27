from django.db import models
from carsmanager.models import Car

ACC = "ACCEPTED"
CANC = "CANCELLED"
PEND = "PENDING"
RET = "RETURNED"

STATUS = ((ACC, "ACCEPTED"),
          (PEND, "PENDING"),
          (CANC, "CANCELLED"),
          (RET, "RETURNED"),
          )


def uploaded_to(int, filename):
    return ("images/licenses/" + int.first_name + "_" + int.last_name + filename)


class Driver(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.IntegerField()
    age = models.IntegerField()

    driver_license = models.ImageField(
        upload_to=uploaded_to, width_field="width_length", height_field="heigth_length", null=True, blank=True)
    width_length = models.IntegerField(default=0, null=True, blank=True)
    heigth_length = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)


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
