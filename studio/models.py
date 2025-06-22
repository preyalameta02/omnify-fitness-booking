from django.db import models

class FitnessClass(models.Model):
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField()  # store as UTC
    instructor = models.CharField(max_length=50)
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.datetime} ({self.instructor})"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.fitness_class.name} by {self.client_email}"
