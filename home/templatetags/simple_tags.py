from django.template import Library
from home.models import Category

register = Library()

@register.simple_tag
def allCategories():
    return Category.objects.all()

