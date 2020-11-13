__author__ = 'derek'

from datetime import datetime

from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser,models.Model):

    gender_choices = (
        ('male','男'),
        ('female','女')
    )

    nick_name = models.CharField('昵称',max_length=50,default='')
    birthday = models.DateField('生日',null=True,blank=True)
    gender = models.CharField('性别',max_length=10,choices=gender_choices,default='male')
    adress = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Banner(models.Model):
    '''
    轮播图
    '''
    title = models.CharField('标题',max_length=100)
    image = models.ImageField('轮播图',upload_to='banner/%Y%m',max_length=100)
    url = models.URLField('访问地址',max_length=200)
    index = models.IntegerField('顺序',default=100)
    add_time = models.DateTimeField('添加时间',default=datetime.now)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name























# class Student(models.Model):
#     '''
#     学生表
#     '''
#     GENDER_CHOICES = (
#         ("male", u"男"),
#         ("female", u"女")
#     )
#
#     St_name = models.CharField("姓名",default="",max_length=30,help_text="姓名")
#     St_birthday = models.DateField("出生年月", null=True, blank=True)
#     St_gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
#     St_native_place = models.CharField("籍贯",default="",max_length=30,help_text="籍贯")
#     St_nation = models.CharField("民族",default="",max_length=30,help_text="民族")
#     St_mobile = models.CharField("电话", max_length=11)
#     add_time = models.DateTimeField("添加时间", default=datetime.now)
#
# class Teacher(models.Model):
#     '''
#     教师表
#     '''
#     GENDER_CHOICES = (
#         ("male", u"男"),
#         ("female", u"女")
#     )
#     Tr_name = models.CharField("姓名", default="", max_length=30, help_text="姓名")
#     Tr_gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
#     Tr_age =models.IntegerField("年龄",max_length=6,default=0)
#     Tr_position = models.CharField("职位", default="", max_length=30, help_text="职位")
#     add_time = models.DateTimeField("添加时间", default=datetime.now)
#
# class Course(models.Model):
#     '''
#     课程表
#     '''
#     Ce_title = models.CharField("课程名称", default="", max_length=30, help_text="课程名称")
#     Ce_name = models.CharField("课程讲师", default="", max_length=30, help_text="课程讲师")
#
#
# class Grade_table(models.Model):
#     '''
#     成绩表
#     '''
#
#     Ce_id = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name="课程id")
#     St_id = models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name="学生id")
#     Grade = models.FloatField("学习成绩",default=0)


