from django.contrib import admin

# Register your models here.
from .models import *
import xadmin
# Register your models here.


class TeacherAdmin(object):
    list_display = ("name","work_years","work_company","work_position","points","click_nums","fav_nums","add_time")
    # 搜索的字段，不要添加时间搜索
    search_fields = ['name','work_company','work_position']
    # 过滤
    list_filter = ['name','work_company','work_position']
xadmin.site.register(Teacher,TeacherAdmin)