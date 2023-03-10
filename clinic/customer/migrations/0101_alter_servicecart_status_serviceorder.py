# Generated by Django 4.1.5 on 2023-03-06 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0100_servicecart_addons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecart',
            name='status',
            field=models.CharField(choices=[('in-cart', 'in-cart'), ('booked', 'booked'), ('removed', 'removed')], default='in-cart', max_length=20),
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('cost', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('order-confirmed', 'order-confirmed'), ('in-progress', 'in-progress'), ('awaiting-user', 'awaiting-user'), ('cancelled', 'cancelled'), ('rejected', 'rejected'), ('delivered', 'delivered'), ('refunded', 'refunded'), ('completed', 'completed')], default='order-placed', max_length=200)),
                ('cart', models.ManyToManyField(to='customer.servicecart')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
