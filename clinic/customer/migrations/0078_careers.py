# Generated by Django 4.1.4 on 2023-01-05 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0077_careeropenings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('country', models.CharField(max_length=300)),
                ('zip_code', models.CharField(max_length=300)),
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('company_awareness', models.CharField(max_length=300)),
                ('ever_applied', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('ever_applied_yes', models.CharField(max_length=300)),
                ('applied_date', models.DateTimeField()),
                ('ever_employed', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('ever_employed_yes', models.CharField(max_length=300)),
                ('employed_date', models.DateTimeField()),
                ('school', models.CharField(max_length=300)),
                ('shool_compl_year', models.DateField()),
                ('college', models.CharField(max_length=300)),
                ('college_compl_year', models.DateField()),
                ('college_course', models.CharField(max_length=300)),
                ('university', models.CharField(max_length=300)),
                ('cosmet_school', models.CharField(max_length=300)),
                ('cosmet_compl_year', models.DateField()),
                ('cosmet_course', models.CharField(max_length=300)),
                ('massage_school', models.CharField(max_length=300)),
                ('massage_compl_year', models.DateField()),
                ('massage_course', models.CharField(max_length=300)),
                ('other_school', models.CharField(max_length=300)),
                ('other_compl_year', models.DateField()),
                ('other_course', models.CharField(max_length=300)),
                ('special_training', models.CharField(max_length=300)),
                ('exp_company', models.CharField(max_length=300)),
                ('exp_phone', models.PositiveIntegerField()),
                ('exp_address', models.CharField(max_length=300)),
                ('exp_from', models.DateField()),
                ('exp_to', models.DateField()),
                ('exp_supervisor', models.CharField(max_length=300)),
                ('exp_rate', models.PositiveIntegerField()),
                ('exp_job', models.CharField(max_length=300)),
                ('exp_reason_leave', models.CharField(max_length=300)),
                ('age', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('contact_personal_employer', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('currently_employed', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('law_status', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('drive_license', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('drive_license_exp', models.DateField()),
                ('transportation', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('current_salary', models.PositiveIntegerField()),
                ('need_salary', models.PositiveIntegerField()),
                ('want_salary', models.PositiveIntegerField()),
                ('cuurent_work_hours', models.CharField(max_length=300)),
                ('likely_work_hours', models.CharField(max_length=300)),
                ('client_count', models.PositiveIntegerField()),
                ('strengths', models.CharField(max_length=300)),
                ('areas_improve', models.CharField(max_length=300)),
                ('contr_to_comp', models.CharField(max_length=300)),
                ('contr_subs', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('convicted', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=300)),
                ('mon_hrs', models.CharField(max_length=300)),
                ('tue_hrs', models.CharField(max_length=300)),
                ('wed_hrs', models.CharField(max_length=300)),
                ('thu_hrs', models.CharField(max_length=300)),
                ('fri_hrs', models.CharField(max_length=300)),
                ('sat_hrs', models.CharField(max_length=300)),
                ('sun_hrs', models.CharField(max_length=300)),
                ('ind_exp', models.CharField(max_length=300)),
                ('ind_bg', models.CharField(max_length=300)),
                ('ind_offer', models.CharField(max_length=300)),
                ('ind_expect', models.CharField(max_length=300)),
                ('ind_goals', models.CharField(max_length=300)),
                ('ind_goal_plan', models.CharField(max_length=300)),
                ('ind_where_see', models.CharField(max_length=300)),
                ('ind_exp_years', models.CharField(max_length=300)),
                ('ind_pr_job_exp', models.CharField(max_length=300)),
                ('ind_pr_job_leave', models.CharField(max_length=300)),
                ('ind_crazy', models.CharField(max_length=300)),
                ('ind_how_spa', models.CharField(max_length=300)),
                ('ind_how_no_spa', models.CharField(max_length=300)),
                ('reference', models.CharField(max_length=300)),
                ('resume', models.FileField(max_length=300, upload_to='uploads/')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.careeropenings')),
            ],
        ),
    ]