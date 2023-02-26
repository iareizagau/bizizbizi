from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    mountain_club = models.CharField(max_length=200, null=True, blank=True, verbose_name='Mendi elkartea')
    public = models.BooleanField(null=True, blank=True, verbose_name='Erabiltzaile publikoa')
    log_count = models.PositiveIntegerField(default=0, null=True, blank=True, verbose_name='Saioa hasi kontadorea')
    created = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name='Sortze data')
    updated = models.DateTimeField(null=True, blank=True, auto_now=True, verbose_name='Edizio data')

    class Meta:
        verbose_name = "Profila"
        verbose_name_plural = "Profilak"
        ordering = ['user__username']

    def __unicode__(self):
        return "foo"


def login_user(sender, request, user, **kwargs):
    profiles = Profile.objects.get(user=user)
    profiles.log_count += 1
    # profiles_user = profiles.get(user=self.request.user.id)

    # Profile.log_count = Profile.log_count + 1
    profiles.save()


user_logged_in.connect(login_user)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get("created", False):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")
