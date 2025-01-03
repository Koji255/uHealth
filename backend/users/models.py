from django.db import models

from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.hashers import make_password


ROLES = (
    ('user', 'user'),
    ('doctor', 'doctor'),
)


# Create your models here.
class User(AbstractUser):

    role = models.CharField(max_length=30, default='user', verbose_name='Role',
                            choices=ROLES)

    phone = models.CharField(max_length=15, blank=True, null=True, unique=False,
                             verbose_name='Phone Number')

    birthday = models.DateField(blank=True, null=True, verbose_name='Birthday')

    email_confirmed = models.BooleanField(default=False)


    def __str__(self):
        return self.username
    

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        if len(self.username) == 0:
            self.username = self.email

        super().save(*args, **kwargs)
        
        # if self.pk:
        #     users_group = Group.objects.get_or_create(name="users")

        #     self.groups.set([users_group])


    class Meta:

        verbose_name= 'User'
        verbose_name_plural = 'Users'