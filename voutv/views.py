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
from voutv.models import post,livtv
#end

#serializer 
from voutv.api.serializers import Rootapiviews
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
    queryset               = post.objects.all().order_by('-id')
    serializer_class       = Rootapiviews
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['authors__author_name','title','details','catagry__author_name']
    pagination_class       = StandardResultsSetPagination