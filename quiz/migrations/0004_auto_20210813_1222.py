# Generated by Django 3.0.5 on 2021-08-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_course_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='time',
            field=models.IntegerField(help_text='time for quiz in minutes'),
        ),
    ]
