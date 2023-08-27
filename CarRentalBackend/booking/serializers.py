from rest_framework import serializers
from .models import Booking, Driver


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'pick_up_date', 'return_date', 'booked_car',
                  'booked_driver', "status")


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'first_name', 'last_name', 'email',
                  'phone_number', 'age')
