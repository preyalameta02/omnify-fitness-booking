from rest_framework import serializers
from .models import FitnessClass, Booking
from django.utils import timezone

class FitnessClassSerializer(serializers.ModelSerializer):
    datetime_ist = serializers.SerializerMethodField()

    class Meta:
        model = FitnessClass
        fields = ['id', 'name', 'datetime', 'datetime_ist', 'instructor', 'available_slots']

    def get_datetime_ist(self, obj):
        return timezone.localtime(obj.datetime).isoformat()

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email', 'booked_at']
