# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('date_listed', models.DateTimeField(verbose_name='Date Listed')),
                ('date_exchanged', models.DateTimeField(verbose_name='Date Exchanged')),
                ('date_fallthrough', models.DateTimeField(verbose_name='Date Fsllen Through')),
                ('list_price', models.IntegerField(default=0)),
                ('sale_price', models.IntegerField(default=0)),
                ('commission', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='team_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.Team'),
        ),
    ]
