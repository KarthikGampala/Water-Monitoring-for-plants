# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-05 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0003_humidity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moisture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moi_value', models.CharField(max_length=250)),
            ],
        ),
    ]
