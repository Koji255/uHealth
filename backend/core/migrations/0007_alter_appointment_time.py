# Generated by Django 5.1.4 on 2024-12-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_appointment_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateTimeField(blank=True, default='', null=True, verbose_name='Назначенное Время'),
        ),
    ]
