# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-25 13:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='AddEvent',
        ),
    ]
