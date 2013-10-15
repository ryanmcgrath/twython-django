#!/usr/bin/env python

import os
import sys

from setuptools import setup
from setuptools import find_packages

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '1.5.2'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='twython-django',
    version=__version__,
    install_requires=['twython>=3.1.0', 'django'],
    author='Ryan McGrath',
    author_email='ryan@venodesigns.net',
    license=open('LICENSE').read(),
    url='https://github.com/ryanmcgrath/twython-django/tree/master',
    keywords='twitter search api tweet twython stream django integration',
    description='Django Integration for Twython -- the actively maintained, pure Python wrapper for the Twitter API. Supports both normal and streaming Twitter APIs',
    long_description=open('README.rst').read(),
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet'
    ]
)
