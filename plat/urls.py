from django.urls import path
from plat import views

urlpatterns = [
    path('add_goods/', views.add_goods, name="add_goods"),
    path('delete_goods/', views.delete_goods, name="delete_goods"),
]