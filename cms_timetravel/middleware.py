

class TimetravelMiddleware(object):

    def process_request(self, request):
        from datetime import datetime
        from cms_timetravel.utils import set_timetravel_date
        set_timetravel_date(request.session.get('timetravel_date', datetime.now()))
