# Generated by Django 4.1.2 on 2022-12-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0036_alter_contactus_messsage'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeslots',
            name='date',
            field=models.DateField(null=True),
        ),
    ]