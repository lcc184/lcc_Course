from django.contrib import admin

# Register your models here.
from .models import *
import xadmin
# Register your models here.
class UserCourseAdmin(object):
    exclude = ( "add_time",)
    list_display = ("user","course",)





class CourseCommentsAdmin(object):
    exclude = ("add_time",)
    list_display = ("user","course","comments",)


class UserFavoriteAdmin(object):
    exclude = ("add_time",)
    list_display = ("user", "fav_id","fav_type",)



xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)