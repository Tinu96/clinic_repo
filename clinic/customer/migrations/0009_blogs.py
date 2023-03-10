# Generated by Django 4.1.4 on 2022-12-19 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_introoffers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]