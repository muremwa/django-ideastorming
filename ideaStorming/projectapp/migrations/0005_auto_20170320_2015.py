# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 00:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_project_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='mark',
            field=models.DecimalField(decimal_places=3, max_digits=4, null=True),
        ),
    ]
