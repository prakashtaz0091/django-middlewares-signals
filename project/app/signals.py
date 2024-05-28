from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Product

# Signal handler for pre_save
@receiver(pre_save, sender=Product)
def product_pre_save(sender, instance, **kwargs):
    # Perform actions before saving the instance
    print("Before saving:", instance.name)

# Signal handler for post_save
@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    # Perform actions after saving the instance
    print("After saving:", instance)
    if created:
        print("Instance created")
        #call notifcation api so that user can get updates
    else:
        print("Instance updated")
