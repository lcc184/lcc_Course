from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from .models import *
from .serializers import UserProfileSerializers,BannerSerializers
class BannerViewSet(APIView):
    '''
    用户信息
    '''
    def get(self,request):
        banner = Banner.objects.all()
        banner_serializer = BannerSerializers(banner, many=True)
        return JsonResponse(banner_serializer,safe=False)