# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 15:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_page', '0026_remove_answer_show_all_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='answer',
            new_name='belong_to',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='comment_user',
        ),
        migrations.AddField(
            model_name='comment',
            name='child_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment', to='site_page.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who_reply', to='site_page.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_ip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote',
            field=models.IntegerField(default=1),
        ),
    ]