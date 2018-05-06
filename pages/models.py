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


def slide_path(instance, filename):
    ext = filename.split('.')[-1]
    wallpaper_name = instance.title.lower().replace(' ', '_')
    return 'static/img/slides/{}.{}'.format(wallpaper_name, ext)


class Slide(Base):
    title = models.CharField(max_length=120)
    description = models.TextField(
        max_length=255,
        blank=True,
        help_text='Short description with less than 255 letters.'
    )
    wallpaper = models.ImageField(
        upload_to=slide_path,
        help_text='Upload a 1440x960 pixel .jpg image.'
    )

    def __str__(self):
        return self.title


def staff_avatar_path(instance, filename):
    ext = filename.split('.')[-1]
    avatar_name = instance.full_name.lower().replace(' ', '_')
    return 'static/img/staffs/{}.{}'.format(avatar_name, ext)


def staff_cv_path(instance, filename):
    ext = filename.split('.')[-1]
    cv_name = instance.full_name.lower().replace(' ', '_')
    return 'static/doc/staffs/{}.{}'.format(cv_name, ext)


class Staff(Base):
    """
    Abstracts staff members of the company
    """
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField('Short bio')
    avatar = models.ImageField(upload_to=staff_avatar_path, blank=True)
    cv = models.FileField(upload_to=staff_cv_path, blank=True)

    def __str__(self):
        return self.full_name


class Process(Base):
    title = models.CharField(max_length=255)
    description = models.TextField()
    picture = models.ImageField(upload_to='static/img/process/')

    class Meta:
        verbose_name_plural = 'Process'

    def __str__(self):
        return self.title


class Service(Base):
    """
    Abstracts a Service object provided by the Company
    """
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

