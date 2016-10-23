# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='status',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
