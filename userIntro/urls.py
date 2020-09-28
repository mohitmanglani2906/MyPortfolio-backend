from django.urls import path
from userIntro import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('me/', views.UserInroduction.as_view()),
    #path('userPic/', views.UserPic.as_view())

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)