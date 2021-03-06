# Generated by Django 2.2.10 on 2020-03-13 15:26

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('man', '0023_auto_20200313_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etsylisting',
            name='listing_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='etsyreceipt',
            name='receipt_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name='etsytransaction',
            name='transaction_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
        migrations.CreateModel(
            name='EtsyUploadJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('jobs_log', models.TextField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('new', 'new'), ('running', 'running'), ('error', 'error'), ('paused', 'paused'), ('finished', 'finished')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('progress', models.CharField(blank=True, max_length=200)),
                ('items_total', models.IntegerField(default=0)),
                ('items_processed', models.IntegerField(default=0)),
                ('job_data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('file_archive', models.FileField(upload_to='%Y/%m/%d/')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='man.EtsyShop')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
