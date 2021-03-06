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
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100



class rootapiview(generics.ListAPIView):
    # permission_classes     = [permissions.IsAuthenticated]
    queryset               = class_note.objects.all().order_by('-id')[:6]
    serializer_class       = class_note_seri
    pagination_class       = StandardResultsSetPagination







class photo_views(generics.ListAPIView):
    queryset               = photo.objects.all().order_by('-id')
    serializer_class       = photos
    pagination_class       = StandardResultsSetPagination



class Academic_Infos_views(generics.ListAPIView):
    queryset               = Academic_Info.objects.all().order_by('-id')
    serializer_class       = Academic_Infos
    pagination_class       = StandardResultsSetPagination
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['title','details']



class livtv_seri_views(generics.ListAPIView):
    queryset               = livtv.objects.all().order_by('-id')
    serializer_class       = livtv_seri
    pagination_class       = StandardResultsSetPagination



class coverimg_seri_views(generics.ListAPIView):
    queryset               = coverimg.objects.all().order_by('-id')[:3]
    serializer_class       = coverimg_seri
    pagination_class       = StandardResultsSetPagination






class Apps_fetures(generics.ListAPIView):
    queryset               = Apps_about.objects.all()
    serializer_class       = appsabot_feture
    pagination_class       = StandardResultsSetPagination




class Apps_itemlist(generics.ListAPIView):
    queryset               = Apps_linkup.objects.all()
    serializer_class       = Apps_linkup_sri
    pagination_class       = StandardResultsSetPagination





class home_notice_bord_cat(generics.ListAPIView):
    queryset               = Notice_bord.objects.all().order_by('-id')
    serializer_class       = Notice_bordss
    pagination_class       = StandardResultsSetPagination





















# HOme page code
class home_notice_bord(generics.ListAPIView):
    queryset               = Notice_bord.objects.all().order_by('-id')[:3]
    serializer_class       = Notice_bordss
    pagination_class       = StandardResultsSetPagination




class photo_views_home(generics.ListAPIView):
    queryset               = photo.objects.all().order_by('-id')[:3]
    serializer_class       = photos
    pagination_class       = StandardResultsSetPagination





class Academic_Infos_views_home(generics.ListAPIView):
    queryset               = Academic_Info.objects.all().order_by('-id')[:6]
    serializer_class       = Academic_Infos
    pagination_class       = StandardResultsSetPagination







class class_note_seri_views_home(generics.ListAPIView):
    queryset               = class_note.objects.all().order_by('-id')
    serializer_class       = class_note_seri
    pagination_class       = StandardResultsSetPagination




class apps_StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100




class Apps_slidesr(generics.ListAPIView):
    queryset               = Apps_slider.objects.all()[:5]
    serializer_class       = Apps_slider_seri
    pagination_class       = apps_StandardResultsSetPagination


