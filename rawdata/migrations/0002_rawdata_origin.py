# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawdata',
            name='origin',
            field=models.SlugField(default='neolook'),
        ),
    ]