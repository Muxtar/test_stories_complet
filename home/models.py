from typing import Iterable, Optional
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from django.utils.translation import gettext_lazy as _
User = get_user_model()

# Create your models here.

# CREATE TABLE Contact (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(30) NOT NULL,
#     email VARCHAR(50) NOT NULL,
#     subject VARCHAR(30) NOT NULL, 
#     message TEXT NOT NULL
# )

class Base(models.Model):
    class Meta:
        abstract = True

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)


class Contact(Base):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.IntegerField(choices=[(1, _('Suggestion')), (2, _('Complain')), (3, _('Purpose'))])
    message = models.TextField()

    def __str__(self) -> str:
        return f'{self.email} -- {self.subject}'
    
class AboutUs(Base):
    address = models.CharField(max_length=100)
    number = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=40)

class Category(Base):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='category/')
    slug = models.SlugField(max_length=50, null = True, blank = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name} {self.id}")
        return super().save(args, kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class Tag(Base):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
class Story(Base):
    user = models.ForeignKey(User, related_name='story', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='story', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='story', blank=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='stories/')
    cover_image = models.ImageField(upload_to='stories/cover_image/')
    desc = RichTextField()
    slug = models.SlugField(max_length=100, null = True, blank = True)

    def __str__(self) -> str:
        return self.title
    

class Subcribe(Base):
    email = models.EmailField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.email
    

