import os
import sys
import django
import pytz
from datetime import datetime, timedelta

# Dynamically set the path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
sys.path.append(PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_booking.settings')
django.setup()

from studio.models import FitnessClass

FitnessClass.objects.all().delete()

classes = [
    ("Yoga", datetime.now() + timedelta(days=1), "Anjali", 10),
    ("Zumba", datetime.now() + timedelta(days=2), "Priya", 8),
    ("HIIT", datetime.now() + timedelta(days=3), "Rahul", 12),
]

for name, dt, instructor, slots in classes:
    FitnessClass.objects.create(
        name=name,
        datetime=dt.astimezone(pytz.UTC),
        instructor=instructor,
        available_slots=slots
    )

print("✅ Seed data inserted.")
