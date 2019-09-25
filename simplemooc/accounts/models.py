from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Username', max_length=30, unique=True)
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Name', max_length=100, blank=True)
    is_active = models.BooleanField('Is it active?', blank=True, default=True)
    is_staff = models.BooleanField('Is from the team?', blank=True, default=True)
    date_joined = models.DateTimeField('Joined Date', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return  str(self)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
