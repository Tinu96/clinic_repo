# Generated by Django 4.1.4 on 2023-01-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0067_alter_notifications_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_type', models.CharField(choices=[('$', '$')], default='$', max_length=20)),
            ],
        ),
    ]
