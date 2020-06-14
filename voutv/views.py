from django.shortcuts import render
#rest_framwork
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins,filters
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser

#end
import random
import datetime
#user model
from voutv.models import *
#end

#serializer 
from voutv.api.serializers import *
#end

# end



#user filter
from django.contrib.auth import get_user_model
User = get_user_model()
#end

#list view -> APi
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 13
    page_size_query_param = 'page_size'
    max_page_size = 100



class rootapiview(generics.ListAPIView):
    queryset               = Notice_bord.objects.all().order_by('-id')
    serializer_class       = Notice_bordss
    pagination_class       = StandardResultsSetPagination







class photo_views(generics.ListAPIView):
    queryset               = photo.objects.all().order_by('-id')
    serializer_class       = photos
    pagination_class       = StandardResultsSetPagination



class Academic_Infos_views(generics.ListAPIView):
    queryset               = Academic_Info.objects.all().order_by('-id')
    serializer_class       = Academic_Infos
    pagination_class       = StandardResultsSetPagination



class livtv_seri_views(generics.ListAPIView):
    queryset               = livtv.objects.all().order_by('-id')
    serializer_class       = livtv_seri
    pagination_class       = StandardResultsSetPagination



class coverimg_seri_views(generics.ListAPIView):
    queryset               = coverimg.objects.all().order_by('-id')[:3]
    serializer_class       = coverimg_seri
    pagination_class       = StandardResultsSetPagination


class class_note_seri_views(generics.ListAPIView):
    queryset               = class_note.objects.all().order_by('-id')
    serializer_class       = class_note_seri
    pagination_class       = StandardResultsSetPagination





class Apps_fetures(generics.ListAPIView):
    queryset               = class_note.objects.all()
    serializer_class       = appsabot_feture
    pagination_class       = StandardResultsSetPagination







































# # class rootapiview(generics.ListAPIView):
# #     queryset               = post.objects.all().order_by('-id')
# #     serializer_class       = Rootapiviews
# #     filter_backends        = [filters.SearchFilter]
# #     search_fields          = ['authors__author_name','title','details','catagry__author_name']
# #     pagination_class       = StandardResultsSetPagination



# class Content_owners(generics.RetrieveAPIView):
#      queryset               = cetagry.objects.order_by('-id')
#      serializer_class       = ContensstOwner
#      lookup_field           = ('cat_name')

