.. image::  https://travis-ci.org/jjanssen/django-cms-timetravel.png?branch=master
    :target: http://travis-ci.org/jjanssen/django-cms-timetravel
    :alt: build-status

django-cms-timetravel
=====================

About django-cms-timetravel
---------------------------

Django CMS provides previewing of non-published pages. With preview an user can check a page before it goes online.
When configuring ``Homepage A`` with an expire date (for eg: 2013-03-04 00:00) and configuring ``Homepage B`` with a publish data (for eg: 2013-03-04 00:00) preview doesn't make the user feel safe about the homepage switch.

So how can a user check whether the new homepage switch will be picked up correctly?
That's where Django CMS Timetravel arrives at the scene!

Screenshot
----------

.. figure:: https://github.com/jjanssen/django-cms-timetravel/raw/master/docs/images/timetravel.png


Installation
------------

Install django-cms-timetravel with pip::

    $ pip install -e http://github.com/jjanssen/django-cms-timetravel#egg=django-cms-timetravel

.. or::

..     $ pip install django-cms-timetravel


Configuration
-------------

Add the following to your settings file:

    * Add ``cms_timetravel`` to ``INSTALLED_APPS``
    * Add ``cms_timetravel.middleware.TimetravelMiddleware`` to ``MIDDLEWARE_CLASSES``::

        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms_timetravel.middleware.TimetravelMiddleware',


URL Configuration
^^^^^^^^^^^^^^^^^

You need to include the `cms_timetravel.urls` urlpatterns in your root url configuration, for e.g.::

    url(r'^admin/timetravel/$', include('cms_timetravel.urls', namespace='cms_timetravel')),
    ...
    (r'^admin/', include(admin.site.urls)),
