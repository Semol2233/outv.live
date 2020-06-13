from rest_framework import serializers
from voutv.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.pagination import PageNumberPagination



class Notice_bordss(serializers.ModelSerializer):
    class Meta:
        model = Notice_bord
        fields = [
            'id',
            'title',
            'img',
            'release_date'
        ]


class photos(serializers.ModelSerializer):
    class Meta:
        model = photo
        fields = [
            'id',
            'title',
            'img',
            'release_date'

        ]


class Academic_Infos(serializers.ModelSerializer):
    class Meta:
        model = Academic_Info
        fields = [
            'id',
            'title',
            'slug',
            'details',
            'img',
            'release_date'


        ]




class livtv_seri(serializers.ModelSerializer):
    class Meta:
        model = livtv
        fields = [
            'id',
            'live_tv_url',
            'live_logo',
            'channel_name',
            'release_date'

        ]


class coverimg_seri(serializers.ModelSerializer):
    class Meta:
        model = coverimg
        fields = [
            'id',
            'coverimg',
            'img_title',
            'release_date'

        ]

class class_note_seri(serializers.ModelSerializer):
    class Meta:
        model = class_note
        fields = [
            'id',
            'title',
            'slug',
            'details',
            'document',
            'release_date'

        ]



# class Rootapiviews(serializers.HyperlinkedModelSerializer):
#     authors = authorsname(read_only=True)
#     catagry = catgryname(read_only=True)

#     class Meta:
#         model = post
#         fields =[
#             'authors',
#             'catagry',
#             'id',
#             'title',
#             'details',
#             'post_img',
#             'post_view'
#         ]






# #UserAc & User reletet all Data api -> Data relestion  UserDettails
# class UseracAlldata(serializers.ModelSerializer):
#      authors = serializers.CharField(source='authors.author_name')
#      class Meta:
#         model = post
#         fields = [
#             'id',
#             'authors',
#             'title',
#             'slug',
#             'details',
#             'post_img',
#             'front_end_date',  


        


# #root_content_owner
# class ContensstOwner(serializers.HyperlinkedModelSerializer):
#     Data = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = cetagry
#         fields = [
#           'id',
#           'cat_name',
#           'Data'
#         ]
#     def get_Data(self,obj):
#         qs = obj.post_set.all()[:25]
#         return UseracAlldata(qs,many=True).data

