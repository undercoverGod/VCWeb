# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0064_auto_20180105_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storekeeper',
            name='Store_Name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Boarder'),
        ),
    ]
