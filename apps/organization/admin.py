from django.contrib import admin

# Register your models here.
from .models import *


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name","work_years","work_company","work_position","points","click_nums","fav_nums","add_time")

admin.site.register(Teacher,TeacherAdmin)