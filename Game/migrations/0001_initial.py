# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-14 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(default='none', max_length=1000)),
                ('platform', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=5, max_length=10)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_being_scored', to='Game.Game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_scores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
