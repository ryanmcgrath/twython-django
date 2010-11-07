from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
	"""
		An example Profile model that handles storing the oauth_token and
		oauth_secret in relation to a user. Adapt this if you have a current
		setup, there's really nothing special going on here.
	"""
	user = models.ForeignKey(User)
	oauth_token = models.CharField(max_length = 200)
	oauth_secret = models.CharField(max_length = 200)
