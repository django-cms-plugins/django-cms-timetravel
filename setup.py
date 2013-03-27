#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import dirname, join
import os
import sys

# When creating the sdist, make sure the django.mo file also exists:
if 'sdist' in sys.argv:
    try:
        os.chdir('cms_timetravel')
        from django.core.management.commands.compilemessages import compile_messages
        compile_messages(sys.stderr)
    finally:
        os.chdir('..')


setup(
    name='django-cms-timetravel',
    version='1.1.3',
    license='Apache License, Version 2.0',

    install_requires=[
        'django-cms>=2.3.4',
    ],
    requires=[
        'Django (>=1.4)',
    ],
    tests_require=[
        'mock==1.0.1',
    ],

    description='Adds timetravelling functionality to Django CMS',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    author='Janneke Janssen',
    author_email='janneke.janssen@gmail.com',

    url='https://github.com/jjanssen/django-cms-timetravel',
    download_url='https://github.com/jjanssen/django-cms-timetravel/zipball/master',

    packages=find_packages(exclude=('example*',)),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],

    test_suite = 'runtests',
)
