from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
    
    user_help = "The user the profile is associated with."
    user = models.ForeignKey(User, help_text=user_help)
    
    bio_help = "The main text of the post."
    bio = models.TextField(help_text=bio_help)
    
    def __unicode__(self):
        return self.user.username

# signal to handle creating a profile (our extended data) when a user is created.

@receiver(signals.post_save, sender=User)
def user_post_save(sender, instance, signal, *args, **kwargs):
    # Creates user profile
    profile, new = UserProfile.objects.get_or_create(user=instance)