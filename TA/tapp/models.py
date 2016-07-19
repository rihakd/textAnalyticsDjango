import datetime

from django.db import models
from django.utils import timezone


class Essay(models.Model):
    essay_text = models.CharField(max_length=1000)
    essay_title = models.CharField(max_length=200, default='Some Title')
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=30, default='anonymous')

    def __unicode__(self):
    	return self.essay_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Meta:
        permissions = (
            ('view_essay', 'View essay'),
        )


class Comment(models.Model):
    essay = models.ForeignKey(Essay)
    comment_text = models.CharField(max_length=200)
    start_i = models.IntegerField(default=0)
    end_i = models.IntegerField(default=0)
    author = models.CharField(max_length=30, default='anonymous')

    def __unicode__(self):
    	return self.comment_text