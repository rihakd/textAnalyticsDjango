# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0002_auto_20151030_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='essay_title',
            field=models.CharField(default=b'Some Title', max_length=200),
        ),
    ]
