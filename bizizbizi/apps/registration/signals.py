from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Profile


@receiver(user_logged_in)
def user_logged(sender, request, user, **kwargs):
    user.profile.log_count += 1
    user.profile.save()
