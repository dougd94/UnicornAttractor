# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-06 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0007_feature_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='price',
        ),
    ]