# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mess', '0003_boarder_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boarder',
            old_name='date',
            new_name='presence_date',
        ),
    ]