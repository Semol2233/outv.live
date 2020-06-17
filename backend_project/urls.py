
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
urlpatterns = [
    path('simple',include('account_admin_app.urls')),

    path('sdvcsdcdcsdfder43543wrfwefcsf',include('voutv.urls')),
    # path('dd',include('livetv.urls')),


    path('admin', admin.site.urls),
    path('login',obtain_auth_token,name='token_auth' ),
    path('reg', include('rest_auth.registration.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),


    # path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
