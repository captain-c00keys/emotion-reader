# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 00:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emotion_emotions', '0002_emotion_date_recorded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emotions', to=settings.AUTH_USER_MODEL),
        ),
    ]
