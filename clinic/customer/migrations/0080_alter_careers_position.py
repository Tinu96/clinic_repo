# Generated by Django 4.0.6 on 2023-01-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0079_alter_careers_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careers',
            name='position',
            field=models.CharField(max_length=300),
        ),
    ]
