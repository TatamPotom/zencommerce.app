# Generated by Django 2.2.6 on 2019-11-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0012_etsylisting_jobs_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etsylisting',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
