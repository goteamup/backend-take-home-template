from django.db import models


class Booking(models.Model):
    class_session = models.ForeignKey("classes.ClassSession", on_delete=models.CASCADE)
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
