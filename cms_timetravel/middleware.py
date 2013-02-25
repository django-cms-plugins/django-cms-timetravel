

class TimetravelMiddleware(object):

    def process_request(self, request):
        from cms.utils import timezone
        from cms_timetravel.utils import set_timetravel_date
        set_timetravel_date(request.session.get('timetravel_date', timezone.now()))
