# Move along, nothing to see here
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Schedulable(models.Model):
    """
    Abstract model mixin for adding publication start and end date to a CMS
    plugin.

    The plugin rendering logic checks if a CMS plugin instance is an instance
    of this class. If so, its "published" state depends on the dates that have
    been set.
    """
    publication_date = models.DateTimeField(_('publication date'), null=True, blank=True, help_text=_('When the plugin should go live.'), db_index=True)
    publication_end_date = models.DateTimeField(_('publication end date'), null=True, blank=True, help_text=_('When to expire the plugin. Leave empty to never expire.'), db_index=True)

    class Meta:
        abstract = True
