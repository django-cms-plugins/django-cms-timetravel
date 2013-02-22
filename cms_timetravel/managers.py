import logging
from django.conf import settings
from django.db.models import Q

from cms.models.query import PageQuerySet
from cms_timetravel.utils import get_timetravel_date


def published(self, site=None):
    """
    Get all published items from Django CMS Pages and
    filter them according to the actual Timetravel date.
    """
    pub = self.on_site(site).filter(published=True)
    ref_date = get_timetravel_date()

    if settings.CMS_SHOW_START_DATE:
        pub = pub.filter(
            Q(publication_date__lt=ref_date) |
            Q(publication_date__isnull=True)
        )

    if settings.CMS_SHOW_END_DATE:
        pub = pub.filter(
            Q(publication_end_date__gte=ref_date) |
            Q(publication_end_date__isnull=True)
        )

    logging.debug('Retrieving CMS Published pages with date {0}'.format(ref_date))
    return pub


def expired(self):
    """
    Get all expired items from Django CMS Pages and
    filter them according to the actual Timetravel date.
    """
    ref_date = get_timetravel_date()
    logging.debug('Retrieving CMS Expired pages with date {0}'.format(ref_date))
    return self.on_site().filter(publication_end_date__lte=ref_date)

PageQuerySet.published = published
PageQuerySet.expired = expired
