# Generated by Django 4.1.2 on 2022-12-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0029_package_alter_mypackages_package'),
        ('owner', '0006_remove_package_timeslot'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Package',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
