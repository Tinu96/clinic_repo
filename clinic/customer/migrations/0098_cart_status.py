# Generated by Django 4.1.5 on 2023-03-04 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0097_servicecart_cost_servicecart_date_servicecart_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(default='in-cart', max_length=20),
        ),
    ]
