from django.urls import path,re_path
from django.conf.urls import url
from plat import views

urlpatterns = [
    re_path(r'^plat/$', views.plat_goods, name="plat_goods"),
    re_path(r'^add_goods/$', views.add_goods, name="add_goods"),
    re_path(r'^edit_goods/$', views.edit_goods, name="edit_goods"),
    re_path(r'^del_(?P<pk>\d+)/$', views.del_goods, name="del_goods"),
    #path('delete_goods/', views.delete_goods, name="delete_goods"),
]