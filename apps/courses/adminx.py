from django.contrib import admin
from .models import Course
import xadmin
# Register your models here.
class CourseAdmin(object):
    list_display = ("name","desc","detail","students","fav_nums","image","click_nums","add_time")
    # 搜索的字段，不要添加时间搜索
    search_fields = ['name']
    # 过滤
    list_filter = ['name',]

xadmin.site.register(Course,CourseAdmin)