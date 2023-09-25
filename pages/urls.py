
from django.urls import path
from . import views

urlpatterns = [

    path('', views.info, name='info'),
    path('content/', views.index, name='index'),
    path('login/', views.login, name='login'),

]
