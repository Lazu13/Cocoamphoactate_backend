# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FriendsPending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('platform', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GameLib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cocoamphoactate.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cocoamphoactate.Game')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cocoamphoactate.User'),
        ),
        migrations.AddField(
            model_name='gamelib',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cocoamphoactate.User'),
        ),
        migrations.AddField(
            model_name='friendspending',
            name='user_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_that_send_invitation', to='Cocoamphoactate.User'),
        ),
        migrations.AddField(
            model_name='friendspending',
            name='user_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_that_has_to_accept', to='Cocoamphoactate.User'),
        ),
        migrations.AddField(
            model_name='friends',
            name='user_one',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sending_invitation', to='Cocoamphoactate.User'),
        ),
        migrations.AddField(
            model_name='friends',
            name='user_two',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_receiving_invitation', to='Cocoamphoactate.User'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_game', to='Cocoamphoactate.Game'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_having_fav_game', to='Cocoamphoactate.User'),
        ),
    ]
