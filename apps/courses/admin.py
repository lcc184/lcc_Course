from django.contrib import admin
from .models import Course
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name","desc","detail","students","fav_nums","image","click_nums","add_time")


admin.site.register(Course,CourseAdmin)