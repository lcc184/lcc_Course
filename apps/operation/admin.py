from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ("user","course","add_time")


class CourseCommentsAdmin(admin.ModelAdmin):
    list_display = ("user","course","comments","add_time")


class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ("user","fav_id","fav_type","add_time")


admin.site.register(UserCourse,UserCourseAdmin)
admin.site.register(UserFavorite,UserFavoriteAdmin)
admin.site.register(CourseComments,CourseCommentsAdmin)