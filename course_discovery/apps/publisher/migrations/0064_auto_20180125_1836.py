# Generated by Django 1.11.3 on 2018-01-25 18:36


import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20171004_1133'),
        ('publisher', '0063_auto_20171219_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEntitlement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('mode', models.CharField(choices=[('verified', 'Verified'), ('professional', 'Professional')], max_length=63, verbose_name='Course mode')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='version',
            field=models.IntegerField(default=0, verbose_name='Workflow Version'),
        ),
        migrations.AddField(
            model_name='historicalcourse',
            name='version',
            field=models.IntegerField(default=0, verbose_name='Workflow Version'),
        ),
        migrations.AddField(
            model_name='courseentitlement',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entitlements', to='publisher.Course'),
        ),
        migrations.AddField(
            model_name='courseentitlement',
            name='currency',
            field=models.ForeignKey(default='USD', on_delete=django.db.models.deletion.CASCADE, related_name='publisher_entitlements', to='core.Currency'),
        ),
        migrations.AlterUniqueTogether(
            name='courseentitlement',
            unique_together={('course', 'mode')},
        ),
    ]
