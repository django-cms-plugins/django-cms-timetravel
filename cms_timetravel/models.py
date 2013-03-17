from django.db import models
from django.utils.translation import ugettext_lazy as _


class Schedulable(models.Model):
    """
    Abstract model mixin for adding publication start and end date to a CMS
    plugin.

    The plugin rendering logic checks if a CMS plugin instance is an instance
    of this class.
    If so, its "published" state depends on the dates that have been set.

    Example of usage:

    .. code-block:: python

        from django.db import models
        from cms.models import CMSPlugin
        from cms_timetravel.models import Schedulable

        class TimetravelPlugin(CMSPlugin, Schedulable):
            title = models.CharField('title', max_length=50)
            body_text = models.TextField('text')

    """
    publication_date = models.DateTimeField(_('publication date'), null=True, blank=True, help_text=_('When the plugin should go live.'), db_index=True)
    publication_end_date = models.DateTimeField(_('publication end date'), null=True, blank=True, help_text=_('When to expire the plugin. Leave empty to never expire.'), db_index=True)

    class Meta:
        abstract = True
