# Generated by Django 4.1.2 on 2022-12-22 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0026_alter_services_timeslots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='timeslots',
            field=models.ManyToManyField(null=True, to='customer.timeslots'),
        ),
    ]