# Generated by Django 4.0.6 on 2023-01-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0094_bannerimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bannerimage',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='image2',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='bannerimage',
            name='image3',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
