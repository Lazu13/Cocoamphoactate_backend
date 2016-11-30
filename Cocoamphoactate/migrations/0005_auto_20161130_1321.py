# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-30 12:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cocoamphoactate', '0004_auto_20161130_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_scores', to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
