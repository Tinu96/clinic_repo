# Generated by Django 4.1.4 on 2022-12-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0034_timeslots_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='messsage',
            field=models.CharField(max_length=500),
        ),
    ]