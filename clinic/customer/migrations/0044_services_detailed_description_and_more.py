# Generated by Django 4.1.4 on 2022-12-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0043_rename_messsage_contactus_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='detailed_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='services',
            name='detailed_information',
            field=models.TextField(blank=True, null=True),
        ),
    ]
