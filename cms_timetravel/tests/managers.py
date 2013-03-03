from datetime import datetime
from django.test.testcases import TestCase

from cms.api import create_page
from cms.models import Page
from cms_timetravel.utils import set_timetravel_date


class TimetravelManagerTest(TestCase):

    def setUp(self):
        self._create_pages()

    def _create_pages(self):
        self.date3 = datetime(2013, 03, 11)
        self.page3 = create_page('test page 3', 'dummy.html', 'en-us', published=True, publication_date=self.date3)

        self.date2 = datetime(2013, 03, 10)
        self.page2 = create_page('test page 2', 'dummy.html', 'en-us', published=True, publication_date=self.date2)

        self.date1 = datetime(2013, 03, 03)
        self.page1 = create_page('test page 1', 'dummy.html', 'en-us', published=True, publication_date=self.date1)

    def testPageThree(self):
        set_timetravel_date(datetime(2013, 03, 11, 0, 0, 1))
        pages = Page.objects.published()

        self.assertEqual(pages.count(), 3)
        self.assertEqual(self.page3, pages.get_home())

    def testPageTwo(self):
        set_timetravel_date(datetime(2013, 03, 10, 0, 0, 1))
        pages = Page.objects.published()

        self.assertEqual(pages.count(), 2)
        self.assertEqual(self.page2, pages.get_home())

    def testPageOne(self):
        set_timetravel_date(datetime(2013, 03, 03, 0, 0, 1))
        pages = Page.objects.published()

        self.assertEqual(pages.count(), 1)
        self.assertEqual(self.page1, pages.get_home())
