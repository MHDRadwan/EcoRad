# shop/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Customer

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created and instance.is_active:
        Customer.objects.get_or_create(user=instance,
                                       defaults={'name': instance.username, 'email': instance.email})