# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rawdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.TextField()),
                ('uri', models.CharField(max_length=50)),
                ('createtime', models.DateTimeField()),
                ('pubtime', models.DateField()),
            ],
        ),
    ]
