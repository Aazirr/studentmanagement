# Generated by Django 5.0.4 on 2024-05-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_alter_grade_unique_together_alter_grade_enrollment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='final_grade',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='midterm_grade',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]
