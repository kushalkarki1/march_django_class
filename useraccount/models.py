from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avtar = models.ImageField(upload_to="avtar/", null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    bank_branch = models.CharField(max_length=255, null=True, blank=True)
    bank_account = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)