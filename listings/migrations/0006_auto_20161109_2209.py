# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20161109_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date_exchanged',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Exchanged'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date_fallthrough',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date Fallen Through'),
        ),
    ]
