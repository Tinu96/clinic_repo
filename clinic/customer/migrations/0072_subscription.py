# Generated by Django 4.1.4 on 2023-01-04 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0071_alter_currency_currency_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]