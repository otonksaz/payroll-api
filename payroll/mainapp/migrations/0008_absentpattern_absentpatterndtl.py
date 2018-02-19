# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-19 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20180218_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsentPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patternCd', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AbsentPatternDtl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.IntegerField()),
                ('status', models.BooleanField()),
                ('timeIn', models.TimeField()),
                ('timeOut', models.TimeField()),
                ('breakIn', models.TimeField()),
                ('breakOut', models.TimeField()),
                ('absentPattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='absentPatternDtls', to='mainapp.AbsentPattern')),
            ],
        ),
    ]
