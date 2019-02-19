from django.urls import path,re_path
from accounts import views
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('myself/', views.myself, name="myself"),
    path('myself_edit/', views.myself_edit, name="myself_edit"),
    path('signup/', views.signup, name="signup"),
    path('headimg/', views.headimg, name='user_img'),
    re_path(r'^user_(?P<id>\d+)/$', views.user_profile, name="user_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)