# Generated by Django 4.1.4 on 2022-12-30 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0056_alter_services_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='rating',
            field=models.FloatField(default=5),
        ),
    ]
