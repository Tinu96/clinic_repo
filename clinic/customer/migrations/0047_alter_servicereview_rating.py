# Generated by Django 4.1.4 on 2022-12-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0046_alter_services_striked_off_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicereview',
            name='rating',
            field=models.PositiveIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], null=True),
        ),
    ]