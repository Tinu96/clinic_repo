# Generated by Django 4.1.2 on 2023-03-09 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0102_forbooking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forbooking',
            old_name='booking_date',
            new_name='bookingdate',
        ),
    ]
