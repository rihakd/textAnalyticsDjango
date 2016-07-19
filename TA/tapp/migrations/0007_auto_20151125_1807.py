# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0006_auto_20151119_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='essay_text',
            field=models.CharField(max_length=1000),
        ),
    ]
