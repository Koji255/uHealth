# Generated by Django 5.1.4 on 2024-12-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_appointment_spezialisation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name': 'Appointment', 'verbose_name_plural': 'Appointments'},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Created'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='specialization',
            field=models.CharField(choices=[('unknown', 'unknown'), ('therapist', 'therapist'), ('pediatrician', 'pediatrician'), ('otolaryngologist', 'otolaryngologist'), ('surgeon', 'surgeon'), ('cardiologist', 'cardiologist'), ('neurologist', 'neurologist'), ('endocrinologist', 'endocrinologist'), ('ophthalmologist', 'ophthalmologist'), ('dermatologist', 'dermatologist'), ('psychiatrist', 'psychiatrist'), ('psychotherapist', 'psychotherapist'), ('dentist', 'dentist'), ('urologist', 'urologist'), ('gynecologist', 'gynecologist'), ('oncologist', 'oncologist'), ('resuscitator', 'resuscitator'), ('anesthesiologist', 'anesthesiologist'), ('hematologist', 'hematologist'), ('gastroenterologist', 'gastroenterologist'), ('infectious disease specialist', 'infectious disease specialist'), ('rheumatologist', 'rheumatologist'), ('pulmonologist', 'pulmonologist'), ('nephrologist', 'nephrologist'), ('allergist', 'allergist'), ('immunologist', 'immunologist'), ('mammologist', 'mammologist'), ('traumatologist', 'traumatologist'), ('phlebologist', 'phlebologist'), ('proctologist', 'proctologist'), ('venereologist', 'venereologist'), ('neurosurgeon', 'neurosurgeon'), ('gerontologist', 'gerontologist'), ('arrhythmologist', 'arrhythmologist'), ('ultrasound specialist', 'ultrasound specialist'), ('physiotherapist', 'physiotherapist'), ('nutritionist', 'nutritionist'), ('speech therapist', 'speech therapist'), ('podiatrist', 'podiatrist'), ('orthopedist', 'orthopedist')], default='unknown', max_length=50, verbose_name='Doctors Specialization'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('in progress', 'in progress'), ('closed', 'closed')], default='pending', max_length=11, verbose_name='Appointment Status'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Appointment Time'),
        ),
    ]