from django.db import models

MAL = "Male"
FEM = "Female"

GENDER = ((MAL, "Male"),
          (FEM, "Female")
          )


def uploaded_to(int, filename):
    return ("images/licenses/" + int.first_name + "_" + int.last_name + filename)


class Driver(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=200, choices=GENDER)
    price_per_day = models.IntegerField(null=True, blank=True)
    is_customer = models.BooleanField(default=False)

    driver_license = models.ImageField(
        upload_to=uploaded_to, width_field="width_length", height_field="heigth_length", null=True, blank=True)
    width_length = models.IntegerField(default=0, null=True, blank=True)
    heigth_length = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)
