from django.contrib import admin
from .models import FitnessClass, Booking

class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'instructor', 'available_slots', 'datetime')
    search_fields = ('name', 'instructor__username')

class BookingClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'fitness_class', 'client_name', 'client_email', 'booked_at')
    search_fields = ('fitness_class', 'client_name')

admin.site.register(FitnessClass, FitnessClassAdmin)
admin.site.register(Booking, BookingClassAdmin)
