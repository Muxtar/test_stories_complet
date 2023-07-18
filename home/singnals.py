from django.db.models.signals import pre_save, post_save
from home.models import Story
from django.utils.text import slugify
from django.dispatch import receiver

@receiver(post_save, sender = Story)
def StorySignal(sender, instance, created,*args, **kwargs):
    if created:
        instance.slug = slugify(f"{instance.title} {instance.id}")
        instance.save()

