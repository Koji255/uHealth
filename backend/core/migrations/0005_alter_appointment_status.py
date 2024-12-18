# Generated by Django 5.1.4 on 2024-12-18 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_appointment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('ожидание', 'ожидание'), ('исполнение', 'исполнение'), ('закрыто', 'закрыто')], default='ожидание', max_length=10, verbose_name='Статус Заявки'),
        ),
    ]
