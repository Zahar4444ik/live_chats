from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('<slug:slug>/clean_chat/', views.clean_chat, name='clean_chat')
]