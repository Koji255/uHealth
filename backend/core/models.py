from django.core.exceptions import ValidationError
from django.db import models

from users.models import User



STATUSES = (
    ('pending', 'pending'),
    ('in progress', 'in progress'),
    ('closed', 'closed'),
)

SPECIALIZATIONS = (
    ('unknown', 'unknown'),
    ('therapist', 'therapist'),
    ('pediatrician', 'pediatrician'),
    ('otolaryngologist', 'otolaryngologist'),
    ('surgeon', 'surgeon'),
    ('cardiologist', 'cardiologist'),
    ('neurologist', 'neurologist'),
    ('endocrinologist', 'endocrinologist'),
    ('ophthalmologist', 'ophthalmologist'),
    ('dermatologist', 'dermatologist'),
    ('psychiatrist', 'psychiatrist'),
    ('psychotherapist', 'psychotherapist'),
    ('dentist', 'dentist'),
    ('urologist', 'urologist'),
    ('gynecologist', 'gynecologist'),
    ('oncologist', 'oncologist'),
    ('resuscitator', 'resuscitator'),
    ('anesthesiologist', 'anesthesiologist'),
    ('hematologist', 'hematologist'),
    ('gastroenterologist', 'gastroenterologist'),
    ('infectious disease specialist', 'infectious disease specialist'),
    ('rheumatologist', 'rheumatologist'),
    ('pulmonologist', 'pulmonologist'),
    ('nephrologist', 'nephrologist'),
    ('allergist', 'allergist'),
    ('immunologist', 'immunologist'),
    ('mammologist', 'mammologist'),
    ('traumatologist', 'traumatologist'),
    ('phlebologist', 'phlebologist'),
    ('proctologist', 'proctologist'),
    ('venereologist', 'venereologist'),
    ('neurosurgeon', 'neurosurgeon'),
    ('gerontologist', 'gerontologist'),
    ('arrhythmologist', 'arrhythmologist'),
    ('ultrasound specialist', 'ultrasound specialist'),
    ('physiotherapist', 'physiotherapist'),
    ('nutritionist', 'nutritionist'),
    ('speech therapist', 'speech therapist'),
    ('podiatrist', 'podiatrist'),
    ('orthopedist', 'orthopedist'),
)


# Create your models here.
class Appointment(models.Model):

    time = models.DateTimeField(blank=True, null=True, auto_now=False, auto_now_add=False,
                                verbose_name='Appointment Time')
    
    status = models.CharField(max_length=11, choices=STATUSES, default='pending', verbose_name='Appointment Status')
    
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')

    specialization = models.CharField(max_length=50, default='unknown',
                                      choices=SPECIALIZATIONS,
                                      verbose_name='Medical Specialization')
    
    comment = models.TextField(blank=True, null=True, verbose_name='Comment')
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
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'