from django.conf.urls.defaults import *

# your_app = name of your root djang app.
urlpatterns = patterns('your_app.twython_django_oauth.views',
	
	# First leg of the authentication journey...
	(r'^login/?$', "begin_auth"),

	# Logout, if need be
	(r'^/logout?$', "logout"), # Calling logout and what not
	
	# This is where they're redirected to after authorizing - we'll
	# further (silently) redirect them again here after storing tokens and such.
	(r'^thanks/?$', "thanks"),

	# An example view using a Twython method with proper OAuth credentials. Clone
	# this view and url definition to get the rest of your desired pages/functionality.
	(r'^user_timeline/?$', "user_timeline"),
)
