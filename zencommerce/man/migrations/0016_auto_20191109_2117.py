# Generated by Django 2.2.6 on 2019-11-09 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0015_etsylisting_suggested_taxonomy_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etsylisting',
            name='item_weight_unit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
