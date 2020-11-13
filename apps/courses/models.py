from datetime import datetime

from django.db import models

# Create your models here.
# class Course(models.Model):
#     '''
#     课程表
#     '''
#     Ce_title = models.CharField("课程名称", default="", max_length=30, help_text="课程名称")
#     Ce_name = models.CharField("课程讲师", default="", max_length=30, help_text="课程讲师"

class Course(models.Model):
    name = models.CharField("课程名",max_length=50)
    desc = models.CharField("课程描述",max_length=300)
    detail = models.TextField("课程详情")
    students = models.IntegerField("学习人数",default=0)
    fav_nums = models.IntegerField("收藏人数",default=0)
    image = models.ImageField("封面图",upload_to="courses/image/%Y/%m",max_length=100)
    click_nums = models.IntegerField("点击数",default=0)
    add_time = models.DateTimeField("添加时间",default=datetime.now,)

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name