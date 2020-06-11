from rest_framework import serializers
from voutv.models import post,livtv,cetagry,author
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.pagination import PageNumberPagination



class catgryname(serializers.ModelSerializer):
    class Meta:
        model = cetagry
        fields = [
            'id',
            'cat_name'
        ]


class authorsname(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = [
            'id',
            'author_name'
        ]





class Rootapiviews(serializers.HyperlinkedModelSerializer):
    authors = authorsname(read_only=True)
    catagry = catgryname(read_only=True)

    class Meta:
        model = post
        fields =[
            'id',
            'authors',
            'catagry',
            'title',
            'details',
            'post_img',
            'post_view'
        ]


# #detilsapiview
# class DRFPostSdderializer(serializers.HyperlinkedModelSerializer):
#      contentowners   = ContentOwner(read_only=True)
#      channel         = UserPublicSrtilizer(read_only=True)
#      mobilebrand     = BrandProfileInfo(read_only=True)
#      class Meta:
#         model = PostCreate
#         fields = [
#             'channel',
#             'contentowners',
#             'id',
#             'title',
#             'details',
#             'photo',
#             'mobilebrand',
#             'slug',
#             'view',
#             'release_date',
#             'tag',
#             'contentlock',
#             'contentlenth',
#             'contentlink',
#             'Persentase',
#             'reviewcount'

#         ]
#         lookup_field = 'slug'
#         read_only_fields = ['details','Persentase','title','slug','tag','photo','contentlenth','contentlock','contentlink']
        
