from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Session


@receiver(post_save, sender=Session)
def after_saving_session(sender, created, instance, *args, **kwargs):
    """Change all academic sessions to false if this is true"""
    print('True')
    if instance.current is True:
        Session.objects.exclude(pk=instance.id).update(current=False)