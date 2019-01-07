from django.urls import path,re_path
from django.conf.urls import url
from plat import views

urlpatterns = [

    re_path(r'^plat_(?P<pk>\d+)/$', views.plat_goods, name="plat_goods"),
    re_path(r'^plat_(?P<pk>\d+)/add_goods/$', views.add_goods, name="add_goods"),
    #path('add_goods/',views.add_goods, name="add_goods"),
    path('delete_goods/', views.delete_goods, name="delete_goods"),
]