from django.db import models
from cms.models import CMSPlugin
from cms_timetravel.models import Schedulable


class TimetravelPlugin(CMSPlugin, Schedulable):
    title = models.CharField('title', max_length=50)
    body_text = models.TextField('text')

    def __unicode__(self):
        return self.title
