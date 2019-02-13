from django.urls import path,re_path
from plat import views
from django.conf.urls import include, url
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.plat_goods, name="plat_goods"),
    re_path(r'^add_goods/$', views.add_goods, name="add_goods"),
    re_path(r'^edit_(?P<id>\d+)/$', views.edit_goods, name="edit_goods"),
    re_path(r'^del_(?P<id>\d+)/$', views.del_goods, name="del_goods"),
    re_path(r'^good_(?P<id>\d+)/$', views.good_detail, name="good_detail"),
    re_path(r'^loved_(?P<id>\d+)/$', views.loved, name="loved"),
    re_path(r'^unloved_(?P<id>\d+)/$', views.unloved, name="unloved"),
    re_path(r'^love_good/$', views.love_goods, name="love_goods"),
    re_path(r'^my_good/$', views.my_good, name="my_good"),
    re_path(r'^delpost_(?P<id>\d+)/$', views.delete_post, name="delete_post"),
    re_path(r'^replypost_(?P<id>\d+)/$', views.reply_post, name="reply_post"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)