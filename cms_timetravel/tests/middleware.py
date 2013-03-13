from mock import Mock
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase

from cms.utils import timezone
from ..middleware import TimetravelMiddleware
from ..utils import reset_timetravel_date, get_timetravel_date


class TimetravelMiddlewareTest(TestCase):

    def setUp(self):
        self.tm = TimetravelMiddleware()
        self.request = Mock()
        self.request.session = {}

        reset_timetravel_date()
        self._create_superuser()

    def _create_superuser(self):
        User.objects.create_superuser('superuser', 'test@example.com', 'test')

    def test_process_request_without_timetravel(self):
        self.assertEqual(self.tm.process_request(self.request), None)
        self.assertEqual(get_timetravel_date().strftime('%Y-%m-%d %H:%I'), timezone.now().strftime('%Y-%m-%d %H:%I'))

    def test_process_request_with_timetravel(self):
        self.request.session = {'timetravel_date': timezone.datetime(2013, 03, 04, 14, 8, 0)}
        self.request.user = authenticate(username='superuser', password='test')

        self.assertEqual(self.tm.process_request(self.request), None)
        self.assertEqual(str(get_timetravel_date()), '2013-03-04 14:08:00')
