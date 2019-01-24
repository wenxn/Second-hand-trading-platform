from django.urls import path,re_path
from django.conf.urls import url
from plat import views

urlpatterns = [
    re_path(r'^$', views.plat_goods, name="plat_goods"),
    re_path(r'^add_goods/$', views.add_goods, name="add_goods"),
    re_path(r'^edit_(?P<id>\d+)/$', views.edit_goods, name="edit_goods"),
    re_path(r'^del_(?P<id>\d+)/$', views.del_goods, name="del_goods"),
    re_path(r'^good_(?P<id>\d+)/$', views.good_detail, name="good_detail"),
    #path('delete_goods/', views.delete_goods, name="delete_goods"),
]