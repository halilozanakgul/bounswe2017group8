# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-24 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConcertifyApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=36)),
                ('address', models.CharField(blank=True, default='', max_length=24)),
                ('latitude', models.FloatField()),
                ('longtitude', models.FloatField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterField(
            model_name='musician',
            name='genre',
            field=models.CharField(blank=True, default='', max_length=24),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default='defaultuser', max_length=24),
        ),
    ]
