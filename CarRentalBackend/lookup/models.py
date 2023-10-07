from django.db import models

class Car_Brand(models.Model):
    brand = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.brand
    
    
class Car_Categories(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.category = self.category.upper()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category

class Car_Engines(models.Model):
    engine = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.engine = self.engine.upper()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.engine

class Car_Transmission(models.Model):
    transmission = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.transmission = self.transmission.upper()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.transmission


class Car_Model(models.Model):
    maker = models.ForeignKey(Car_Brand, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.model


class Car_Color(models.Model):
    color = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.color
