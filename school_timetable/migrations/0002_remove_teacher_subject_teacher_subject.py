# Generated by Django 5.0.1 on 2024-01-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_timetable', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ManyToManyField(to='school_timetable.subject'),
        ),
    ]
