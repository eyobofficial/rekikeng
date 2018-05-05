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


class Company(Base):
    """
    Abstracts a Company object
    """
    name = models.CharField(
        'Company full name',
        max_length=60,
        help_text=''
    )
    tagline = models.CharField('Company tagline', max_length=255)
    # fevicon = models.ImageField(upload_to='fevicons/')
    quote = models.TextField()
    quote_speaker = models.CharField(
        'Featured quote speaker',
        max_length=60,
        default='Unkown',
    )
    description1 = models.TextField()
    description2 = models.TextField()
    location = models.CharField('Location name', max_length=100)
    subcity = models.CharField(max_length=100)
    city = models.CharField(max_length=100, default='Addis Ababa')
    country = models.CharField(max_length=100, default='Ethiopia')
    email = models.EmailField(max_length=100)
    phone = models.CharField('Phone number', max_length=20)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.name


class Services(Base):
    full_title = models.CharField(max_length=120)
    short_title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.short_title
