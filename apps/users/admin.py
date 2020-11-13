from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("username","birthday","gender","email","mobile","image")


class BannerAdmin(admin.ModelAdmin):
    list_display = ("title","image","url","index","add_time")

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Banner,BannerAdmin)