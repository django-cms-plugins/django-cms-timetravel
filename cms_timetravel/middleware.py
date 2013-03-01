

class TimetravelMiddleware(object):

    def process_request(self, request):
        from cms_timetravel.utils import set_timetravel_date
        if request.session.get('timetravel_date'):
            set_timetravel_date(request.session['timetravel_date'])
