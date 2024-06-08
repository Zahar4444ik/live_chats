from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/rooms/', permanent=True)),
    path('login/', views.sign_in, name='login'),
    path('register/', views.sign_up, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_account/', views.my_account, name='my_account'),
]