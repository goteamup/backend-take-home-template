from rest_framework import viewsets

from .serializers import CustomerSerializer
from .models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
