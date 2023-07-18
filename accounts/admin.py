from django.contrib import admin
from django.contrib.auth import get_user_model
from accounts.models import Profile, BlockUser, Ip
# Register your models here.

admin.site.register([Profile, BlockUser, Ip])