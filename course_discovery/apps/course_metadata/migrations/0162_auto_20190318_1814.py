# Generated by Django 1.11.15 on 2019-03-18 18:14


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_partner_lms_commerce_api_url'),
        ('course_metadata', '0161_curriculum_course_run_exclusions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courserun',
            options={},
        ),
        migrations.AddField(
            model_name='course',
            name='draft',
            field=models.BooleanField(default=False, help_text='Is this a draft version?'),
        ),
        migrations.AddField(
            model_name='courseentitlement',
            name='draft',
            field=models.BooleanField(default=False, help_text='Is this a draft version?'),
        ),
        migrations.AddField(
            model_name='courserun',
            name='draft',
            field=models.BooleanField(default=False, help_text='Is this a draft version?'),
        ),
        migrations.AddField(
            model_name='image',
            name='draft',
            field=models.BooleanField(default=False, help_text='Is this a draft version?'),
        ),
        migrations.AddField(
            model_name='person',
            name='draft',
            field=models.BooleanField(default=False, help_text='Is this a draft version?'),
        ),
        migrations.AddField(
            model_name='seat',
            name='draft',
            field=models.BooleanField(default=False, help_text='Is this a draft version?'),
        ),
        migrations.AddField(
            model_name='video',
            name='draft',
            field=models.BooleanField(default=False, help_text='Is this a draft version?'),
        ),
        migrations.AlterField(
            model_name='courserun',
            name='key',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='video',
            name='src',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='course',
            unique_together={('partner', 'uuid', 'draft'), ('partner', 'key', 'draft')},
        ),
        migrations.AlterUniqueTogether(
            name='courseentitlement',
            unique_together={('course', 'mode', 'draft')},
        ),
        migrations.AlterUniqueTogether(
            name='courserun',
            unique_together={('key', 'draft')},
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together={('src', 'draft')},
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together={('partner', 'uuid', 'draft')},
        ),
        migrations.AlterUniqueTogether(
            name='seat',
            unique_together={('course_run', 'type', 'currency', 'credit_provider', 'draft')},
        ),
        migrations.AlterUniqueTogether(
            name='video',
            unique_together={('src', 'draft')},
        ),
    ]
