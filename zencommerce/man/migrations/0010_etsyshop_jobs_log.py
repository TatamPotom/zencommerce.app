# Generated by Django 2.2.6 on 2019-11-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0009_auto_20191109_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='etsyshop',
            name='jobs_log',
            field=models.TextField(blank=True),
        ),
    ]
