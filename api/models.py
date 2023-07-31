from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    # Add any additional fields you want in your custom user model
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    # Add any custom methods or overrides as needed
    def __str__(self):
        return self.username