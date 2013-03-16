#!/usr/bin/env python

# Django environment setup:
from django.conf import settings, global_settings as default_settings
from django.core.management import call_command
from os.path import dirname, realpath
import sys

# Detect location and available modules
module_root = dirname(realpath(__file__))

# Inline settings file
settings.configure(
    DEBUG=False,  # will be False anyway by DjangoTestRunner.
    TEMPLATE_DEBUG=False,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    },
    TEMPLATE_LOADERS=(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
    TEMPLATE_CONTEXT_PROCESSORS = default_settings.TEMPLATE_CONTEXT_PROCESSORS + (
        'django.core.context_processors.request',
    ),
    MIDDLEWARE_CLASSES = default_settings.MIDDLEWARE_CLASSES + (
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',
        'cms_timetravel',
        'mptt',
        'cms',
        'menus',
        'cms_timetravel.tests.testapp',
    ),
    SITE_ID = 1,
    ROOT_URLCONF = 'cms_timetravel.tests.testapp.urls',
    STATIC_URL='/static/',
    CMS_LANGUAGES = (('en-us', 'English'),),
    CMS_TEMPLATES = (('dummy.html', 'Dummy'),),
    CMS_SHOW_START_DATE = True,
    CMS_SHOW_END_DATE = True,
)

call_command('syncdb', verbosity=1, interactive=False)


# ---- app start
verbosity = 2 if '-v' in sys.argv else 1

from django.test.utils import get_runner
TestRunner = get_runner(settings)  # DjangoTestSuiteRunner
runner = TestRunner(verbosity=verbosity, interactive=True, failfast=False)
failures = runner.run_tests(['cms_timetravel'])

if failures:
    sys.exit(bool(failures))