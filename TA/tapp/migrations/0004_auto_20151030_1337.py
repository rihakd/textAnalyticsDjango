# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0003_essay_essay_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='votes',
            new_name='start_i',
        ),
    ]
