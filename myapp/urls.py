from django.urls import path

from .import views



urlpatterns = [

     path('',views.index,name="home"),
     path('flower/<slug:slug>/',views.detail,name="detail"),
     path('tags/<slug:slug>/',views.tags,name="tags"),
     path('flower-create/',views.create,name="creates"),
     path('flower-edit/<int:pk>/',views.edit,name="edit"),
      path('flower-delete/<int:pk>/',views.delete,name="delete"),


]