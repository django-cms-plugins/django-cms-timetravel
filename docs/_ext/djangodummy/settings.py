from django.conf import settings, global_settings as default_settings
# Settings file to allow parsing API documentation of Django modules,
# and provide defaults to use in the documentation.
#
# This file is placed in a subfolder,
# so the docs root is not used by find_packages()

# Display proper URLs in the docs:
TEMPLATE_CONTEXT_PROCESSORS = default_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
INSTALLED_APPS = (
    'cms_timetravel',
    'mptt',
    'cms',
    'menus',
)
SECRET_KEY = 'koetjeboe'
STATIC_URL = '/static/'
CMS_TEMPLATES = ()
