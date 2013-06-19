#!/usr/bin/python

from setuptools import setup
from setuptools import find_packages

__author__ = 'Ryan McGrath <ryan@venodesigns.net>'
__version__ = '1.5.0'

setup(
    name='twython-django',
    version=__version__,
    install_requires=['twython>=3.0.0', 'django'],
    author='Ryan McGrath',
    author_email='ryan@venodesigns.net',
    license=open('LICENSE').read(),
    url='https://github.com/ryanmcgrath/twython/tree/master',
    keywords='twitter search api tweet twython stream django integration',
    description='Actively maintained, pure Python wrapper for the Twitter API. Supports both normal and streaming Twitter APIs',
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
