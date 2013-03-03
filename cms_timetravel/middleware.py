

class TimetravelMiddleware(object):

    def process_request(self, request):
        if request.user.is_authenticated() and 'timetravel_date' in request.session:
            from cms_timetravel.utils import set_timetravel_date
            set_timetravel_date(request.session.get('timetravel_date'))
