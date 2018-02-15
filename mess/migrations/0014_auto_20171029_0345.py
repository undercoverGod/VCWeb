# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 22:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0013_auto_20171028_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('chat_datetime', models.DateTimeField(default=datetime.datetime(2017, 10, 29, 3, 45, 55, 618524))),
            ],
        ),
        migrations.AlterField(
            model_name='boarder',
            name='dp',
            field=models.ImageField(blank=True, upload_to='images/mess'),
        ),
        migrations.AlterField(
            model_name='boarder',
            name='presence_date',
            field=models.DateField(default=datetime.date(2017, 10, 29)),
        ),
        migrations.AddField(
            model_name='chat',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mess.Boarder'),
        ),
    ]