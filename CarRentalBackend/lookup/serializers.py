from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car_Brand
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car_Categories
        fields = '__all__'


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car_Engines
        fields = '__all__'


class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car_Transmission
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car_Color
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car_Model
        fields = '__all__'
