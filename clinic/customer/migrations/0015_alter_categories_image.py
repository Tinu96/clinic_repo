# Generated by Django 4.1.4 on 2022-12-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_alter_categories_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
