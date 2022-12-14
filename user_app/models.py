from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    display_name = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    data_of_birth = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    bio = models.CharField(max_length=512, blank=True, null=True)
    avatar = models.ImageField(upload_to='profile_images/', blank=True, default='profile_images/default.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
