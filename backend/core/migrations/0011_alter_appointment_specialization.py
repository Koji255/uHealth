# Generated by Django 5.1.4 on 2024-12-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_appointment_options_alter_appointment_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='specialization',
            field=models.CharField(choices=[('unknown', 'unknown'), ('therapist', 'therapist'), ('pediatrician', 'pediatrician'), ('otolaryngologist', 'otolaryngologist'), ('surgeon', 'surgeon'), ('cardiologist', 'cardiologist'), ('neurologist', 'neurologist'), ('endocrinologist', 'endocrinologist'), ('ophthalmologist', 'ophthalmologist'), ('dermatologist', 'dermatologist'), ('psychiatrist', 'psychiatrist'), ('psychotherapist', 'psychotherapist'), ('dentist', 'dentist'), ('urologist', 'urologist'), ('gynecologist', 'gynecologist'), ('oncologist', 'oncologist'), ('resuscitator', 'resuscitator'), ('anesthesiologist', 'anesthesiologist'), ('hematologist', 'hematologist'), ('gastroenterologist', 'gastroenterologist'), ('infectious disease specialist', 'infectious disease specialist'), ('rheumatologist', 'rheumatologist'), ('pulmonologist', 'pulmonologist'), ('nephrologist', 'nephrologist'), ('allergist', 'allergist'), ('immunologist', 'immunologist'), ('mammologist', 'mammologist'), ('traumatologist', 'traumatologist'), ('phlebologist', 'phlebologist'), ('proctologist', 'proctologist'), ('venereologist', 'venereologist'), ('neurosurgeon', 'neurosurgeon'), ('gerontologist', 'gerontologist'), ('arrhythmologist', 'arrhythmologist'), ('ultrasound specialist', 'ultrasound specialist'), ('physiotherapist', 'physiotherapist'), ('nutritionist', 'nutritionist'), ('speech therapist', 'speech therapist'), ('podiatrist', 'podiatrist'), ('orthopedist', 'orthopedist')], default='unknown', max_length=50, verbose_name='Medical Specialization'),
        ),
    ]
