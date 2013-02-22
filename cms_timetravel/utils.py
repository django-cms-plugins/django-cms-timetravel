import logging
from datetime import datetime

try:
    from threading import local
except ImportError:
    from django.utils._threading_local import local

# thread local support
_thread_locals = local()


def set_timetravel_date(timetravel_date):
    """
    Assigns current user from request to thread_locals, used by
    CurrentUserMiddleware.
    """
    logging.debug('Setting timetravel date: {0}'.format(timetravel_date))
    _thread_locals.timetravel_date = timetravel_date


def get_timetravel_date():
    timetravel_date = getattr(_thread_locals, 'timetravel_date', datetime.now())
    logging.debug('Getting timetravel date: {0}'.format(timetravel_date))
    return timetravel_date
