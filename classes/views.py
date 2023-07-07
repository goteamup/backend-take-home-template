from rest_framework import viewsets

from .serializers import ClassTypeSerializer, ClassSessionSerializer
from .models import ClassType, ClassSession


class ClassTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ClassTypeSerializer
    queryset = ClassType.objects.all()


class ClassSessionViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSessionSerializer
    queryset = ClassSession.objects.all()
