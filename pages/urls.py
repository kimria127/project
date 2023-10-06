
from django.urls import path
from . import views

urlpatterns = [

    path('info/', views.info, name='info'),
    path('content/', views.index, name='index'),
    path('content-neck/', views.contentN, name='contentN'),
    path('content-ear/', views.contentE, name='contentE'),
    path('content-let/', views.contentL, name='contentL'),

    path('content-neck/neckbuy/<int:product_id>/', views.neckbuy, name='neckbuy'),
    path('content-ear/earbuy/<int:product_id>/', views.earbuy, name='earbuy'),
    path('content-let/letbuy/<int:product_id>/', views.letbuy, name='letbuy'),

]
