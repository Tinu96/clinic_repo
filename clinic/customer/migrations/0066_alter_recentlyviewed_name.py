# Generated by Django 4.0.6 on 2022-12-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0065_recentlyviewed_name_alter_recentlyviewed_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentlyviewed',
            name='name',
            field=models.CharField(max_length=300, null=True, unique=True),
        ),
    ]
