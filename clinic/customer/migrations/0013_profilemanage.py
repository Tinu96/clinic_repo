# Generated by Django 4.1.4 on 2022-12-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_remove_contactus_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=200)),
                ('address', models.TextField()),
                ('contactno', models.PositiveIntegerField()),
                ('company', models.CharField(max_length=200)),
            ],
        ),
    ]