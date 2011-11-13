Twython-Django (An example Django Python Twitter OAuth Application, using Twython)
=========================================================================================
OAuth is an annoying specification to work with. Twitter has an awesome and somewhat unique
real time data stream, though, and it'd be a shame to miss out on that stuff because of the warts
of a specification.

Twython supports OAuth authentication with Twitter now, and this is a sample Django application to get
people up and running (fairly) instantly with Twitter OAuth in Django. Enjoy.


Requirements
-----------------------------------------------------------------------------------------------------
Django - pretty self explanatory. http://djangoproject.com/

Twython - the Python Twitter API wrapper of choice.

    (pip install | easy_install) twython

...or, you can clone the repo and install it the old fashioned way.

    git clone https://ryanmcgrath@github.com/ryanmcgrath/twython.git  
    cd twython
    sudo python setup.py install  

Twython (for versions of Python before 2.6) requires a library called
"simplejson". Depending on your flavor of package manager, you can do the following... 

    (pip install | easy_install) simplejson

Twython also requires the (most excellent) OAuth2 library for handling OAuth tokens/signing/etc. Again...

    (pip install | easy_install) oauth2


Installation
-----------------------------------------------------------------------------------------------------

pip install git+http://github.com/zandeez/twython-django.git

Add "twython_django_oauth" to your "INSTALLED_APPS" in your settings.py file. If you wish to use the example
template, feel free to copy that over as well.

After you've done that, specify the following urlconf in your root urls.py:

    (r'^your_url_extension/', include('twython_django_oauth.urls')),
	
Add the following settings to settings.py:

TWITTER_KEY = 'your_key'
TWITTER_SECRET = 'your_secret'

LOGIN_URL='/your_url_extension/login'
LOGIN_REDIRECT_URL='/'
LOGOUT_URL='/your_url_extension/logout'
LOGOUT_REDIRECT_URL='/'

Restart your Django app, and it should all work auto-magically. Build onwards from here if you're
just starting out, or integrate this into your existing model setup if you're already Django-savvy.

Enjoy!


Need Twython Help?
-----------------------------------------------------------------------------------------------------
If you need help with the Twython library itself, check out the project on Github, it's all pretty self
contained (twython/twitter_endpoints.py contains just about every function definition you'll need):

    https://github.com/ryanmcgrath/twython

Questions, Comments, etc?
-----------------------------------------------------------------------------------------------------
My hope is that twython-django is so simple that you'd never *have* to ask any questions, but if
you feel the need to contact me for this (or other) reasons, you can hit me up 
at ryan@venodesigns.net.

twython-django is released under an MIT License - see the LICENSE file for more information.
