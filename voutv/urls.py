from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from voutv import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', views.rootapiview.as_view()),
    path('photo', views.photo_views.as_view()),
    path('Academic_Info', views.Academic_Infos_views.as_view()),
    path('livetvfedd', views.livtv_seri_views.as_view()),
    path('coverimg', views.coverimg_seri_views.as_view()),
    path('classnote', views.class_note_seri_views.as_view()),


 
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
