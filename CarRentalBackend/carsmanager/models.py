from django.db import models
from django.contrib.auth.models import User
from driver.models import Driver
from lookup.models import Car_Categories, Car_Engines, Car_Transmission, Car_Brand, Car_Color, Car_Model


def uploaded_to(int, filename):
    return ("images/cars/" + filename)


class Car(models.Model):
    name = models.CharField(max_length=200)
    model_year = models.CharField(max_length=200)
    brand = models.ForeignKey(Car_Brand, on_delete=models.SET_NULL, null=True, blank=True)
    plate_number = models.CharField(max_length=200)

    color = models.ForeignKey(Car_Color, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.ForeignKey(Car_Model, on_delete=models.SET_NULL, null=True, blank=True)
    vin = models.CharField(max_length=200, null=True, blank=True)

    # Car features
    category = models.ForeignKey(Car_Categories, on_delete=models.SET_NULL, null=True, blank=True)
    engine_type = models.ForeignKey(Car_Engines, on_delete=models.SET_NULL, null=True, blank=True)
    transmission_type = models.ForeignKey(Car_Transmission, on_delete=models.SET_NULL, null=True, blank=True)

    seat_number = models.IntegerField()
    rate = models.FloatField(null=True, blank=True)

    with_driver = models.BooleanField()
    driver = models.ForeignKey(
        to=Driver, on_delete=models.SET_NULL, null=True, blank=True)
    images = models.ImageField(
        upload_to=uploaded_to, null=True, blank=True)
    width_length = models.IntegerField(default=0, null=True, blank=True)
    heigth_length = models.IntegerField(default=0,  null=True, blank=True)

    owner = models.ForeignKey(User, null=True, blank=True,
                              on_delete=models.CASCADE)

    price_per_day = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # if self.model
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
