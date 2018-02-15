# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0054_auto_20171214_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boarder',
            name='user',
        ),
        migrations.AlterField(
            model_name='presence',
            name='boarder',
            field=models.ManyToManyField(blank=True, to='account.Boarder'),
        ),
        migrations.DeleteModel(
            name='Boarder',
        ),
    ]