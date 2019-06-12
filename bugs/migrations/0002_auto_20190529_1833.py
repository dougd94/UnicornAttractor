# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-29 18:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='published_date',
        ),
        migrations.AddField(
            model_name='bug',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('TD', 'To Do'), ('D', 'Doing'), ('F', 'Finished')], default='TD', max_length=1),
        ),
        migrations.AlterField(
            model_name='bug',
            name='upvotes',
            field=models.DecimalField(decimal_places=1, default='1', max_digits=10),
        ),
    ]
