# Generated by Django 2.2.6 on 2019-11-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='etsylisting',
            name='num_favorers',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='etsylisting',
            name='views',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]