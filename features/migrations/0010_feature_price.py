# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-10 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0009_auto_20190608_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='price',
            field=models.IntegerField(default=50),
        ),
    ]