import logging
from cms.utils import timezone
from threading import local

_thread_locals = local()


def reset_timetravel_date():
    """
    A function to reset the timetravel date within the thread local.
    It sets the date to the current date and time, according to its
    appropriate timezone.
    """
    set_timetravel_date(timezone.now())


def set_timetravel_date(timetravel_date):
    """
    Assigns the timetravel date from request to ``thread_locals``, used by :class:`~cms_timetravel.middleware.TimetravelMiddleware`.

    The basic invocation only requires a datetime object:

    .. code-block:: python

        from cms.utils import timezone
        set_timetravel_date( timezone.datetime(2013, 2, 7, 15, 55, 13) )

    """
    logging.debug('Setting timetravel date: {0}'.format(timetravel_date))
    _thread_locals.timetravel = timetravel_date


def get_timetravel_date():
    """
    Returns the timetravel date from ``thread_locals`` as datetime object.
    If no date is set, it'll return the current date and time according to
    its appropriate timezone.
    """
    timetravel_date = getattr(_thread_locals, 'timetravel', timezone.now())
    return timetravel_date
