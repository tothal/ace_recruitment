# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadfile', '0002_auto_20170109_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='document',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='document',
            name='profession',
            field=models.CharField(blank=True, max_length=45),
        ),
    ]
