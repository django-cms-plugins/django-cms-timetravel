from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from cms.api import create_page
from cms.utils import timezone


class TimetravelAdminTest(TestCase):
    url = reverse('cms_timetravel:timetravel')

    @classmethod
    def setUpClass(self):
        create_page('home', 'dummy.html', 'en-us', published=True)

    def setUp(self):
        self._create_superuser()

    def _create_superuser(self):
        User.objects.create_superuser('superuser', 'test@example.com', 'test')

    def _login(self):
        self.assertTrue(self.client.login(username='superuser', password='test'))

    def _get_timetravel_view(self):
        self._login()
        return self.client.get(self.url)

    def _date(self, date=timezone.now()):
        return date.strftime('%Y-%m-%d')

    def _set_session(self):
        # Work-around in var. self.client.session isn't mutable
        # See also: https://code.djangoproject.com/ticket/10899
        session = self.client.session
        session['timetravel_date'] = timezone.now()
        session.save()

    def test_view_permission(self):
        response_invalid = self.client.get(self.url)
        self.assertEqual(response_invalid.status_code, 302)
        self.assertEqual(response_invalid.get('location'), 'http://testserver/accounts/login/?next=/admin/timetravel/')

        response = self._get_timetravel_view()
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.request['PATH_INFO'], self.url)

    def test_context(self):
        response = self._get_timetravel_view()
        self.assertContains(response, 'Timetravel')
        self.assertContains(response, self._date())
        self.assertContains(response, 'There is currently no time-traveling date set.')

        self._set_session()
        response_date = self._get_timetravel_view()
        self.assertContains(response_date, 'The current timetravel date is:')

    def test_initial(self):
        response = self._get_timetravel_view()
        form = response.context['form']
        self.assertEquals(form.initial['auto_redirect'], True)
        self.assertEquals(self._date(form.initial['timetravel_date']), self._date())

    def test_success_url(self):
        # Test redirect to root
        self._login()
        response = self.client.post(self.url, {
            'timetravel_date_0': '2013-03-04',
            'timetravel_date_1': '14:05:00',
            'auto_redirect': True
        }, follow=True)
        self.assertRedirects(response, reverse('pages-root'), 302, 200)

        # Test redirect to timetravel view
        response_to_self = self.client.post(self.url, {
            'timetravel_date_0': '2013-03-04',
            'timetravel_date_1': '14:05:00',
            'auto_redirect': False
        })
        self.assertRedirects(response_to_self, self.url, 302, 200)

    def test_clear_param(self):
        self._login()
        self._set_session()

        self.assertTrue('timetravel_date' in self.client.session)

        self.client.get(self.url, {'clear': ''})
        self.assertFalse('timetravel_date' in self.client.session)
