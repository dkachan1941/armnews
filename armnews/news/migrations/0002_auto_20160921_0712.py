# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='title',
            new_name='name',
        ),
    ]
