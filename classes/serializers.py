from rest_framework.serializers import ModelSerializer
from classes.models import ClassType, ClassSession


class ClassTypeSerializer(ModelSerializer):
    class Meta:
        model = ClassType
        fields = ["id", "name", "description"]


class ClassSessionSerializer(ModelSerializer):
    class Meta:
        model = ClassSession
        fields = ["id", "class_type", "starts_at"]
