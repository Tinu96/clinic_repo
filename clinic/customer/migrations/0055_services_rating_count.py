# Generated by Django 4.1.4 on 2022-12-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0054_remove_servicereview_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='rating_count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]