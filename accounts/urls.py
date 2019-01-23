from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('myself/', views.myself, name="myself"),
    path('signup/', views.signup, name="signup"),
]