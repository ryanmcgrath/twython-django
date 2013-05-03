#!/usr/bin/python

from setuptools import setup
from setuptools import find_packages

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '1.4.6'

setup(
	# Basic package information.
	name = 'twython-django',
	version = __version__,
	packages = find_packages(),

	# Packaging options.
	include_package_data = True,

	# Package dependencies.
	install_requires = ['simplejson',
                        'oauth2',
                        'httplib2',
                        'twython>=2.7.2',
                        'django'],
	provides = ['twython_django_oauth'],

	# Metadata for PyPI.
	author = 'Ryan McGrath',
	author_email = 'ryan@venodesigns.net',
	license = 'MIT License',
	url = 'http://github.com/ryanmcgrath/twython-django/tree/master',
	keywords = 'Django integration for twython',
	description = 'An easy (and up to date) way to access Twitter data with Python.',
	long_description = open('README.markdown').read(),
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Communications :: Chat',
		'Topic :: Internet'
	]
)
