from rest_framework import serializers

from .models import *

class UserProfileSerializers(serializers.ModelSerializer):
    '''
    用户信息
    '''

    class Meta:
        model = UserProfile
        fields = "__all__"


class BannerSerializers(serializers.ModelSerializer):
    '''
    轮播图
    '''
    class Meta:
        model = Banner
        url = serializers.CharField(source='get_absolute_url', read_only=True)
        fields = "__all__"
