from django.test import TestCase
from .models import FitnessClass, Booking
from datetime import datetime, timedelta
import pytz

class BookingTestCase(TestCase):
    def setUp(self):
        self.fitness_class = FitnessClass.objects.create(
            name="Test Yoga",
            datetime=(datetime.now() + timedelta(days=1)).astimezone(pytz.UTC),
            instructor="Test Instructor",
            available_slots=2
        )

    def test_booking_success(self):
        Booking.objects.create(
            fitness_class=self.fitness_class,
            client_name="Test User",
            client_email="test@example.com"
        )
        self.assertEqual(Booking.objects.count(), 1)
