# Generated by Django 4.1.2 on 2023-03-10 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0106_rename_user_forbooking_usern'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forbooking',
            old_name='usern',
            new_name='user',
        ),
    ]
