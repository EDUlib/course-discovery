# Generated by Django 3.2.16 on 2022-11-25 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0304_degree_program_duration_override'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degree',
            name='program_duration_override',
        ),
        migrations.AddField(
            model_name='historicalprogram',
            name='program_duration_override',
            field=models.CharField(blank=True, help_text='Useful field to overwrite the duration of a program. It can be a text describing a period of time, Ex: 6-9 months.', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='program',
            name='program_duration_override',
            field=models.CharField(blank=True, help_text='Useful field to overwrite the duration of a program. It can be a text describing a period of time, Ex: 6-9 months.', max_length=20, null=True),
        ),
    ]