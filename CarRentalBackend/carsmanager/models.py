from django.db import models
from django.contrib.auth.models import User
from driver.models import Driver

VAN = "VAN"
SUV = "SUV"
PRE = "PREMIUM"
MID = "MIDSIZE"
SML = "SMALL"

ELEC = "ELECTRIC"
HYBR = "HYBRID"
PETR = "PETROL"
DIES = "DIESEL"

AUTO = "AUTOMATIC"
MANU = "MANUAL"

CATEGORY = ((SML, "SMALL"),
            (MID, "MIDSIZE"),
            (PRE, "PREMIUM"),
            (SUV, "SUV"),
            (VAN, "VAN"),
            )

ENGINE = ((ELEC, "ELECTRIC"),
          (HYBR, "HYBRID"),
          (PETR, "PETROL"),
          (DIES, "DIESEL"),
          )

TRANSMISSION = ((AUTO, "AUTOMATIC"),
                (MANU, "MANUAL"),
                )


def uploaded_to(int, filename):
    return ("images/cars/" + filename)


class Car(models.Model):
    name = models.CharField(max_length=200)
    model_year = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    plate_number = models.CharField(max_length=200)

    # Car features
    with_driver = models.BooleanField()
    category = models.CharField(max_length=200, choices=CATEGORY)
    seat_number = models.IntegerField()
    engine_type = models.CharField(max_length=200, choices=ENGINE)
    transmission_type = models.CharField(max_length=200, choices=TRANSMISSION)
    rate = models.FloatField(null=True, blank=True)

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

    def __str__(self):
        return self.name
