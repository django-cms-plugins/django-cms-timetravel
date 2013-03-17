from django.core.urlresolvers import reverse
from django.test import TestCase
from cms.api import create_page, add_plugin
from cms.utils import timezone
from cms_timetravel.utils import reset_timetravel_date
from cms_timetravel.utils import set_timetravel_date


class TimetravelPublishedManagerTest(TestCase):

    def setUp(self):
        self._create_example()
        self.page_url = reverse('pages-root')

    def tearDown(self):
        reset_timetravel_date()

    def _create_example(self):
        self.page = create_page('Example Page', 'dummy.html', 'en-us', published=True, publication_date=timezone.datetime(2013, 2, 14))
        placeholder = self.page.placeholders.get(slot='content')
        add_plugin(placeholder, 'CMSTimetravelPlugin', 'en-us',
            title='Hello',
            body_text='hello world',
            publication_date=timezone.datetime(2013, 3, 16),
            publication_end_date=timezone.datetime(2013, 3, 18)
        )

    def _invalid_contents(self, response):
        self.assertNotContains(response, '<h4>Hello</h4>')
        self.assertNotContains(response, '<p>hello world</p>')

    def _valid_contents(self, response):
        self.assertContains(response, '<h4>Hello</h4>')
        self.assertContains(response, '<p>hello world</p>')

    def test_not_published(self):
        set_timetravel_date(timezone.datetime(2013, 3, 15))
        response = self.client.get(self.page_url)
        self._invalid_contents(response)

    def test_published(self):
        set_timetravel_date(timezone.datetime(2013, 3, 16, 15, 5, 0))
        response = self.client.get(self.page_url)
        self._valid_contents(response)

    def test_published_2(self):
        set_timetravel_date(timezone.datetime(2013, 3, 17, 15, 5, 0))
        response = self.client.get(self.page_url)
        self._valid_contents(response)

    def test_expired(self):
        set_timetravel_date(timezone.datetime(2013, 3, 18, 1, 15))
        response = self.client.get(self.page_url)
        self._invalid_contents(response)
