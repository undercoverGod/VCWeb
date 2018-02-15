# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 23:49
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mess', '0025_auto_20171031_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('chat_datetime', models.DateTimeField(default=datetime.datetime(2017, 11, 1, 5, 19, 22, 937566))),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Temp_Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('chat_datetime', models.DateTimeField(default=datetime.datetime(2017, 11, 1, 5, 19, 22, 937566))),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='chat',
            name='username',
        ),
        migrations.AlterField(
            model_name='boarder',
            name='presence_date',
            field=models.DateField(default=datetime.date(2017, 11, 1)),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]