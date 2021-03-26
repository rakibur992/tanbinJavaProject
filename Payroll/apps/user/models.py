from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from Payroll.apps.core.models import BaseModel
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=100, blank=True)

    # roles = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if not self.password:
            password = User.objects.make_random_password()
            self.set_password(password)
        if not self.username:
            self.username = str(uuid4()[:8])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
