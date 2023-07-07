from django.db import models


class ClassType(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()


class ClassSession(models.Model):
    class_type = models.ForeignKey(ClassType, on_delete=models.PROTECT)
    starts_at = models.DateTimeField()
