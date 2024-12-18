from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.
class User(AbstractUser):

    role = models.CharField(max_length=30, default='user', verbose_name='Роль')

    phone = models.CharField(max_length=15, blank=True, null=True, unique=True,
                             verbose_name='Номер Телефона')

    birthday = models.DateField(blank=True, null=True, verbose_name='Дата Рождения')


    def __str__(self):
        return self.username


    class Meta:
        verbose_name, verbose_name_plural = 'Пользователь', 'Пользователи'