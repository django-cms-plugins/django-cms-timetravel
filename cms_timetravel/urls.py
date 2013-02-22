from django.conf.urls.defaults import url, patterns
from cms_timetravel.views import TimetravelView

urlpatterns = patterns('cms_timetravel',
    url(r'^$', TimetravelView.as_view(), name='timetravel'),
)
