from django.db import models
import datetime


class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    created_at = models.DateTimeField(default=datetime.datetime.utcnow)
