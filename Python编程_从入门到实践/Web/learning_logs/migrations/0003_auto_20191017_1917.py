# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-10-17 11:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
