# Generated by Django 4.1.4 on 2022-12-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0044_services_detailed_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='striked_off_cost',
            field=models.PositiveIntegerField(null=True),
        ),
    ]