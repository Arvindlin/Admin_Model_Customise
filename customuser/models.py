from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomManager

GENDER_CHOICE = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=200, unique=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, blank=True)
    contact = models.CharField(max_length=12)
    dob = models.DateField(default=None, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomManager()

    def __str__(self):
        return self.email
