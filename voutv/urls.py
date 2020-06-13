from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from voutv import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', views.rootapiview.as_view()),
    # path('ceatgrydata/<cat_name>', views.Content_owners.as_view()),
 
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
