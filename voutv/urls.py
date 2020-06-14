from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from voutv import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('', views.rootapiview.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/photo', views.photo_views.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/Academic_Info', views.Academic_Infos_views.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/livetvfedd', views.livtv_seri_views.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/coverimg', views.coverimg_seri_views.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/classnote', views.class_note_seri_views.as_view()),


 
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
