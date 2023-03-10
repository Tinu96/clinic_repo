# Generated by Django 4.0.6 on 2023-01-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0082_alter_careers_age_alter_careers_drive_license_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careers',
            name='applied_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='college_compl_year',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='cosmet_compl_year',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='drive_license_exp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='employed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='exp_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='exp_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='massage_compl_year',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='other_compl_year',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='careers',
            name='shool_compl_year',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
