from django.conf.urls.defaults import *

# your_app = name of your root djang app.
urlpatterns = patterns('twython_django_oauth.views',
	
	# First leg of the authentication journey...
	url(r'^login/?$', "begin_auth", name="twitter_login"),

	# Logout, if need be
	url(r'^logout/?$', "logout", name="twitter_logout"), # Calling logout and what not
	
	# This is where they're redirected to after authorizing - we'll
	# further (silently) redirect them again here after storing tokens and such.
	url(r'^thanks/?$', "thanks", name="twitter_callback"),

	# An example view using a Twython method with proper OAuth credentials. Clone
	# this view and url definition to get the rest of your desired pages/functionality.
	url(r'^user_timeline/?$', "user_timeline", name="twitter_timeline"),
)
