from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager, BaseUserManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

class UserManager(AbstractUserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class Profile(AbstractUser):
	PRIVATE = True
	PUBLIC = False
	VISIBILITY_CHOICES = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )
	private = models.BooleanField(default=False)
	name = models.CharField(max_length=20)
	visibility = models.BooleanField(default=PUBLIC, choices=VISIBILITY_CHOICES)
	bio = models.CharField(max_length=150, blank=True, null=True)
	profile_picture = models.ImageField(upload_to='profile_pics', default='default.png', blank=True, null=True)
	objects = UserManager()
	
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
	post_save.connect(create_profile, sender=User)
    