# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-04 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0010_auto_20190603_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='bugpk',
            new_name='bug',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=300),
        ),
    ]
