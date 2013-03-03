django-cms-timetravel
=====================

Adds timetravelling functionality to Django CMS


Installation
------------

Install django-cms-timetravel with pip::

    $ pip install -e http://github.com/jjanssen/django-cms-timetravel#egg=django-cms-timetravel

or::

    $ pip install django-cms-timetravel


Configuration
-------------

Add the following to your settings file:

    * Add ``cms_timetravel`` to ``INSTALLED_APPS``

        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',


URL Configuration
^^^^^^^^^^^^^^^^^

You need to include the `cms_timetravel.urls` urlpatterns in your root url configuration, for e.g.::

    url(r'^admin/timetravel/$', include('cms_timetravel.urls', namespace='cms_timetravel')),
    ...
    (r'^admin/', include(admin.site.urls)),
