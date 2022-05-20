from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('username', views.login, name='login'),
    path('chat', views.chat, name='chat')
]
