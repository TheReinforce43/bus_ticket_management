from django.urls import path 

from user.View.user_view import (
    UserSignUpAPIView,
    UserLoginAPIView,
    UserLogoutAPIView

)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/',UserSignUpAPIView.as_view(),name='user-signup'),
    path('login/',UserLoginAPIView.as_view(),name='user-login'),    
    path('logout/',UserLogoutAPIView.as_view(),name='user-logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)