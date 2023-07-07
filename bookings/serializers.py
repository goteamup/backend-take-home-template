from rest_framework.serializers import ModelSerializer
from bookings.models import Booking


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "customer", "event", "created_at"]
