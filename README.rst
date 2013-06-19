Twython-Django
==============

    (An example Django Python Twitter OAuth Application, using Twython)

OAuth is an annoying specification to work with. Twitter has an awesome and somewhat unique real time data stream, though, and it'd be a shame to miss out on that stuff because of the warts of a specification.

Twython supports OAuth authentication with Twitter now, and this is a sample Django application to get people up and running (fairly) instantly with Twitter OAuth in Django. Enjoy.

Installation
------------

Install `twython-django` via `pip <http://www.pip-installer.org/>`_

.. code-block:: bash

    $ pip install twython-django

or, with `easy_install <http://pypi.python.org/pypi/setuptools>`_

.. code-block:: bash

    $ easy_install twython-django

But, hey... `that's up to you <http://www.pip-installer.org/en/latest/other-tools.html#pip-compared-to-easy-install>`_.

Or, if you want the code that is currently on GitHub

.. code-block:: bash

    git clone git://github.com/ryanmcgrath/twython-django.git
    cd twython
    python setup.py install

Getting Started
---------------

Add ``twython_django_oauth`` to your ``INSTALLED_APPS`` in your ``settings.py`` file.

If you wish to use the example template, feel free to copy that over as well.

Update urls
^^^^^^^^^^^

Specify the following urlconf in your root urls.py:

.. code-block:: python

    (r'^your_url_extension/', include('twython_django_oauth.urls')),

Modify settings.py
^^^^^^^^^^^^^^^^^^

    Add the following settings to your settings.py

.. code-block:: python
    
    TWITTER_KEY = 'your_key'
    TWITTER_SECRET = 'your_secret'

    LOGIN_URL='/your_url_extension/login'
    LOGOUT_URL='/your_url_extension/logout'
    LOGIN_REDIRECT_URL='/'
    LOGOUT_REDIRECT_URL='/'

Need Twython Help?
------------------

If you need help with the Twython library itself, check out the project on Github. It's all pretty self contained (``twython/endpoints.py`` contains just about every function definition you'll need):

https://github.com/ryanmcgrath/twython

Questions, Comments, etc?
-------------------------

My hope is that twython-django is so simple that you'd never *have* to ask any questions, but if you feel the need to contact me for this (or other) reasons, you can hit me up at ryan@venodesigns.net.

Or contact me on Twitter:

- `@ryanmcgrath <https://twitter.com/ryanmcgrath>`_
