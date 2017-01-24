# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-23 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_page', '0014_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='create_time',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='/avatars/default.png', upload_to='avatars'),
        ),
    ]