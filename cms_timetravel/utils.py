import logging
from cms.utils import timezone

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

_thread_locals = local()


def set_timetravel_date(timetravel_date):
    """
    Assigns current user from request to thread_locals, used by
    CurrentUserMiddleware.
    """
    logging.debug('Setting timetravel date: {0}'.format(timetravel_date))
    _thread_locals.timetravel_date = timetravel_date


def get_timetravel_date():
    """
    Provide the option to get the timetravel date within the application
    """
    timetravel_date = getattr(_thread_locals, 'timetravel_date', timezone.now())
    logging.debug('Getting timetravel date: {0}'.format(timetravel_date))
    return timetravel_date
