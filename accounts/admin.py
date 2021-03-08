from django.contrib import admin
from .models import UserProfile, FriendsGroup

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(FriendsGroup)