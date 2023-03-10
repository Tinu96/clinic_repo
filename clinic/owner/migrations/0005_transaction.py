# Generated by Django 4.1.2 on 2022-12-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0004_alter_memberships_image_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('In Process', 'In Process'), ('Pending', 'Pending'), ('Failed', 'Failed')], max_length=300)),
                ('amount', models.PositiveBigIntegerField()),
                ('currency', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=120)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
