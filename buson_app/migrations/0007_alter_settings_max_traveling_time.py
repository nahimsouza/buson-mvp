# Generated by Django 4.1.2 on 2022-10-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buson_app', '0006_alter_employee_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='max_traveling_time',
            field=models.PositiveIntegerField(verbose_name='Tempo Máximo de Viagem'),
        ),
    ]