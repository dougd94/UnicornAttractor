# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-04 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0013_auto_20190604_1713'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
