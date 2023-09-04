from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return (self.first_name + " " + self.last_name)
