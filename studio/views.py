from rest_framework import generics, status
from rest_framework.response import Response
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

class FitnessClassListView(generics.ListAPIView):
    """
    List all fitness classes ordered by datetime.
    """
    queryset = FitnessClass.objects.all().order_by('datetime')
    serializer_class = FitnessClassSerializer

class BookingCreateView(generics.CreateAPIView):
    """
    Create a booking for a fitness class.
    Decrease the available slots by 1 if the booking is successful.
    """
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        fitness_class_id = request.data.get('fitness_class')
        if not fitness_class_id:
            return Response({'error': 'Missing fitness_class id'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            fc = FitnessClass.objects.get(pk=fitness_class_id)
        except FitnessClass.DoesNotExist:
            return Response({'error': 'Fitness class not found'}, status=status.HTTP_404_NOT_FOUND)

        if fc.available_slots <= 0:
            return Response({'error': 'No available slots.'}, status=status.HTTP_400_BAD_REQUEST)
        
        fc.available_slots -= 1
        fc.save()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookingListView(generics.ListAPIView):
    """
    List all bookings for a specific client based on their email.
    """
    serializer_class = BookingSerializer

    def get(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        if not email:
            return Response(
                {"error": "Email parameter is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        bookings = Booking.objects.filter(client_email=email).order_by('-booked_at')
        if not bookings.exists():
            return Response(
                {"error": f"No bookings found for email: {email}"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
