from django.urls import path
from .views import FitnessClassListView, BookingCreateView, BookingListView

urlpatterns = [
    path('classes/', FitnessClassListView.as_view(), name='list_classes'),
    path('book/', BookingCreateView.as_view(), name='create_booking'),
    path('bookings/', BookingListView.as_view(), name='list_bookings'),
]
