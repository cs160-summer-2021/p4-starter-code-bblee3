# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('qOne', views.qOne, name='qOne'),
    path('qTwo', views.qTwo, name='qTwo'),
    path('qThree', views.qThree, name='qThree'),
    path('qFour', views.qFour, name='qFour'),
    path('qFive', views.qFive, name='qFive'),
    path('bigScreen', views.bigScreen, name='bigScreen'),
    path('bigScreenName', views.bigScreenName, name='bigScreenName'),
    path('thankScreen', views.thankScreen, name='thankScreen'),
]
