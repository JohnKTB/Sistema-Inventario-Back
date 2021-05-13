from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group
from django.db import models

from applications.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    Nombres = models.CharField('Nombres', max_length=30, blank=True)
    ApePat = models.CharField('Apellido Paterno', max_length=30, blank=True)
    ApeMat = models.CharField('Apellido Materno', max_length=30, blank=True)
    NombreCompleto = models.CharField('nombre y apellido', max_length=120, blank=True)
    groups = models.ManyToManyField(Group)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    class Meta:
        db_table = 'auth_user'

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.Nombres + ' ' + self.ApePat
