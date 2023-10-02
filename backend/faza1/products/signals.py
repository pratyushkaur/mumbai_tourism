from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch  import receiver
from .models import Customer, Cart

@receiver(post_save, sender=Customer)
def create_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(customer=instance)

@receiver(post_save, sender=User)
def save_cart(sender,instance,**kwargs):
    instance.profile.save()