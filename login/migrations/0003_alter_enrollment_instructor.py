# Generated by Django 5.0.4 on 2024-05-21 10:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_course_instructor_remove_course_school_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.instructor'),
        ),
    ]