import logging
from cms.utils import timezone

_timetravel = None


def reset_timetravel_date():
    set_timetravel_date(timezone.now())


def set_timetravel_date(timetravel_date):
    """
    Assigns current user from request to thread_locals, used by
    CurrentUserMiddleware.
    """
    global _timetravel
    logging.debug('Setting timetravel date: {0}'.format(timetravel_date))
    _timetravel = timetravel_date


def get_timetravel_date():
    """
    Provide the option to get the timetravel date within the application
    """
    global _timetravel
    logging.debug('Getting timetravel date: {0}'.format(_timetravel))
    return _timetravel if _timetravel else timezone.now()
