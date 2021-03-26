from django.db import models

# Create your models here.


class BaseModel(models.Model):
    """
    It's a abstract model for created_at and modified_at field
    """

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
