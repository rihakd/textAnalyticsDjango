# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0005_comment_end_i'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='essay',
            options={'permissions': (('view_essay', 'View essay'),)},
        ),
    ]
