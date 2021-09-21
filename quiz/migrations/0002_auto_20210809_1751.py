# Generated by Django 3.0.5 on 2021-08-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='total_marks',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='marks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]