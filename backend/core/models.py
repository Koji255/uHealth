# Permissions
# Form number
# Open AI live session
# Email Validation

from django.core.exceptions import ValidationError
from django.db import models

from users.models import User


STATUSES = (
    ('ожидание', 'ожидание'),
    ('исполнение', 'исполнение'),
    ('закрыто', 'закрыто'),
)

# Create your models here.
class Appointment(models.Model):

    time = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False,
                                verbose_name='Назначенное Время')
    
    status = models.CharField(max_length=10, choices=STATUSES, default='ожидание', verbose_name='Статус Заявки')
    
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')

    spezialisation = models.CharField(max_length=50, blank=True, null=True,
                                      verbose_name='Специализация')
    
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    # Relationsheeps custom reverse!
    user = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name='appointment_as_user',
                             blank=True, null=True)
    # Relationsheeps custom reverse!
    doctor = models.ForeignKey(User, on_delete=models.PROTECT, limit_choices_to={'role': 'doctor'},
                               related_name='appointment_as_doctor',
                               blank=True, null=True)


    def __str__(self):
        return f'Appointment with {self.doctor} by {self.user} at {self.time}'
    

    class Meta:
        verbose_name = 'Заявление на прием'
        verbose_name_plural = 'Заявления на прием'