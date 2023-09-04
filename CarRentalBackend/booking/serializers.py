from rest_framework import serializers
from .models import Booking, Driver


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'pick_up_date', 'return_date', 'booked_car',
                  'booked_driver', "status")
