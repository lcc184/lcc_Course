from django.contrib import admin
import xadmin
# Register your models here.
from xadmin import views

from .models import *
# Register your models here.
class UserProfileAdmin(object):
    list_display = ("username","birthday","gender","email","mobile","image")


class BannerAdmin(object):
    list_display = ("title","image","url","index","add_time")

class GlobalSettings(object):
    #全局配置，后台管理标题和页脚
    site_title = "课程机构系统"
    site_footer = "http://127.0.0.1:8000/xadmin/"
    #菜单收缩
    menu_style = "accordion"
xadmin.site.register(Banner,BannerAdmin)


xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(views.CommAdminView, GlobalSettings)