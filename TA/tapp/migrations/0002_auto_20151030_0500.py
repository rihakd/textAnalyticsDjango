# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Question',
            new_name='Essay',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RenameField(
            model_name='essay',
            old_name='question_text',
            new_name='essay_text',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='comment',
            name='essay',
            field=models.ForeignKey(to='tapp.Essay'),
        ),
    ]
