# Generated by Django 5.0.1 on 2024-03-04 15:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='fullname',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, unique=True, verbose_name='Fullname'),
            preserve_default=False,
        ),
    ]