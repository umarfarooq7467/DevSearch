from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver

def createProfile(sender, instance, created, **kwargs):
    print("profile signal trigerred")
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.profile
    print("deleting user")


post_save.connect(createProfile, sender=User)


post_delete.connect(deleteUser, sender=Profile)