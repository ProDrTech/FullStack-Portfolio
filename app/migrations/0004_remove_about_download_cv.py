# Generated by Django 5.2.3 on 2025-06-17 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='download_cv',
        ),
    ]
