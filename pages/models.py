from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Base(models.Model):
    """
    Base model for all other models to inherit from
    """
    created_at = models.DateTimeField(
        'Created date',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        'Modified date',
        auto_now=True
    )

    class Meta:
        abstract = True
