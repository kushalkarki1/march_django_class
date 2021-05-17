from django.db import models
from django.contrib.auth.models import User


class Weight(models.Model):
    weight_range = models.CharField(max_length=255, unique=True)
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.weight_range

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Product(models.Model):
    STATUS_CHOICES = (
        ("pending", "PENDING"),
        ("delivered", "DELIVERED"),
        ("returned", "RETURNED")
    )
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    customer_fullname = models.CharField(max_length=255)
    customer_contact1 = models.CharField(max_length=255)
    customer_contact2 = models.CharField(max_length=255, null=True, blank=True)
    customer_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    remarks = models.TextField(null=True, blank=True)
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.status = "pending"
        super().save(*args, **kwargs)

