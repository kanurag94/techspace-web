# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-25 16:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20180825_1840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddEvent',
            new_name='Event',
        ),
    ]
