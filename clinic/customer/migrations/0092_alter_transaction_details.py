# Generated by Django 4.1.2 on 2023-01-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0091_alter_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='details',
            field=models.CharField(max_length=500),
        ),
    ]
