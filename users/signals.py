# We want a user profile to be created for each user

# this signal is deployed when an object is saved
from django.db.models.signals import post_save
# user is the sender of the signal
from django.contrib.auth.models import User
# receiver
from django.dispatch import receiver
from .models import Profile

# decorator
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    # decorator


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()