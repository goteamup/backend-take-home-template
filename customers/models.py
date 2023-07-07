from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
