# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0004_auto_20151030_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='end_i',
            field=models.IntegerField(default=0),
        ),
    ]
