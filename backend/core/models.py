from django.core.exceptions import ValidationError
from django.db import models

from users.models import User



STATUSES = (
    ('ожидание', 'ожидание'),
    ('исполнение', 'исполнение'),
    ('закрыто', 'закрыто'),
)

SPECIALIZATIONS = (
    ('не известно', 'не известно'),
    ('терапевт', 'терапевт'),
    ('педиатр', 'педиатр'),
    ('отоларинголог', 'отоларинголог'),
    ('хирург', 'хирург'),
    ('кардиолог', 'кардиолог'),
    ('невролог', 'невролог'),
    ('эндокринолог', 'эндокринолог'),
    ('офтальмолог', 'офтальмолог'),
    ('дерматолог', 'дерматолог'),
    ('психиатр', 'психиатр'),
    ('психотерапевт', 'психотерапевт'),
    ('стоматолог', 'стоматолог'),
    ('уролог', 'уролог'),
    ('гинеколог', 'гинеколог'),
    ('онколог', 'онколог'),
    ('реаниматолог', 'реаниматолог'),
    ('анестезиолог', 'анестезиолог'),
    ('гематолог', 'гематолог'),
    ('гастроэнтеролог', 'гастроэнтеролог'),
    ('инфекционист', 'инфекционист'),
    ('ревматолог', 'ревматолог'),
    ('пульмонолог', 'пульмонолог'),
    ('нефролог', 'нефролог'),
    ('аллерголог', 'аллерголог'),
    ('иммунолог', 'иммунолог'),
    ('маммолог', 'маммолог'),
    ('травматолог', 'травматолог'),
    ('флеболог', 'флеболог'),
    ('профтолог', 'профтолог'),
    ('венеролог', 'венеролог'),
    ('нейрохирург', 'нейрохирург'),
    ('геронтолог', 'геронтолог'),
    ('аритмолог', 'аритмолог'),
    ('специалист по УЗИ', 'специалист по УЗИ'),
    ('физиотерапевт', 'физиотерапевт'),
    ('диетолог', 'диетолог'),
    ('логопед', 'логопед'),
    ('подолог', 'подолог'),
    ('ортопед', 'ортопед'),
)


# Create your models here.
class Appointment(models.Model):

    time = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False,
                                verbose_name='Назначенное Время')
    
    status = models.CharField(max_length=10, choices=STATUSES, default='ожидание', verbose_name='Статус Заявки')
    
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата Создания')

    specialization = models.CharField(max_length=50, default='не известно',
                                      choices=SPECIALIZATIONS,
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
    
    
    def save(self, *args, **kwargs):
        comment = self.comment
        
        if len(comment) > 55:
            self.comment = f'{comment[:56]}...'

        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Заявление на прием'
        verbose_name_plural = 'Заявления на прием'