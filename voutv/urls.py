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
    path('sdvcsdcdcsdfder43543wrfwefcsf/Apps_other_data', views.Apps_fetures.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/notice_bord', views.home_notice_bord_cat.as_view()),


    path('sdvcsdcdcsdfder43543wrfwefcsf/slider', views.Apps_slidesr.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/item', views.Apps_itemlist.as_view()),








    path('sdvcsdcdcsdfder43543wrfwefcsf/home_notice', views.home_notice_bord.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/photo_views_home', views.photo_views_home.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/Academic_Infos_views_home', views.Academic_Infos_views_home.as_view()),
    path('sdvcsdcdcsdfder43543wrfwefcsf/class_note_seri_views_home', views.class_note_seri_views_home.as_view()),













  
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
