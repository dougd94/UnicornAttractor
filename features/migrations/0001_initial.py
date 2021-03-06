# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-14 11:23
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
            name='Commentf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('description', models.TextField()),
                ('upvotes', models.DecimalField(decimal_places=0, default='0', max_digits=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=50)),
                ('status', models.CharField(choices=[('T', 'To Do'), ('D', 'Doing'), ('F', 'Finished')], default='T', max_length=1)),
                ('paid', models.BooleanField(default=False)),
                ('quantity', models.DecimalField(decimal_places=0, default='1', max_digits=1)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Votesf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.Feature')),
                ('voterf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='commentf',
            name='feature',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='features.Feature'),
        ),
        migrations.AlterUniqueTogether(
            name='votesf',
            unique_together=set([('voterf', 'feature')]),
        ),
    ]
