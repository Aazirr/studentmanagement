# Generated by Django 5.0.3 on 2024-03-17 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_course_instructor_student_enrollment_grades_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Grades',
            new_name='Grade',
        ),
    ]