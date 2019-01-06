from django.urls import path
from plat import views

urlpatterns = [
    path('(?P<pk>\d+)/$', views.plat_goods, name="plat_goods"),
    path('delete_goods/', views.delete_goods, name="delete_goods"),
]