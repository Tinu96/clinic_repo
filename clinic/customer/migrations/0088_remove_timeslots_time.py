# Generated by Django 4.0.6 on 2023-01-07 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0087_timeslots_end_time_timeslots_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeslots',
            name='time',
        ),
    ]
