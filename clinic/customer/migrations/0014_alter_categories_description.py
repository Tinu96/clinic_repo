# Generated by Django 4.1.4 on 2022-12-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_profilemanage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
