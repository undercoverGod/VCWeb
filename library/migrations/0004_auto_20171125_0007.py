# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]