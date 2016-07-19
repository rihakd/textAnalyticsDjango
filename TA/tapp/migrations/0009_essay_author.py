# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0008_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='essay',
            name='author',
            field=models.CharField(default=b'anonymous', max_length=30),
        ),
    ]
