from django.contrib import admin
from home.models import Contact, AboutUs, Category, Tag, Story, Subcribe

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ['name', 'message', 'email', 'subject']
    search_fields = ['email']
    list_filter = ['subject']

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    fields = ['user', 'category', 'tag', 'title', 'image', 'cover_image', 'desc', 'slug']
    search_fields = ['category__name', 'tag__name']
    list_filter = ['category__name']

admin.site.register([AboutUs, Category, Tag, Subcribe])