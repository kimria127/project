
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('info/', views.info, name='info'),
    path('content/', views.index, name='index'),
    path('content-neck/', views.contentN, name='contentN'),
    path('content-ear/', views.contentE, name='contentE'),
    path('content-let/', views.contentL, name='contentL'),

    path('mypage/', views.mypage, name='mypage'),

    path('cart/', views.cart, name='cart'),
    path('content-neck/neckbuy/<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('content-ear/earbuy/<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('content-let/letbuy/<int:product_id>/add_to_cart/', views.add_to_cart, name='add_to_cart'),

    path('content-neck/neckbuy/<int:product_id>/', views.neckbuy, name='neckbuy'),
    path('content-ear/earbuy/<int:product_id>/', views.earbuy, name='earbuy'),
    path('content-let/letbuy/<int:product_id>/', views.letbuy, name='letbuy'),

    path('content-neck/neckbuy/<int:product_id>/comment/', views.comment_create, name='comment_create'),
    path('content-ear/earbuy/<int:product_id>/comment/', views.comment_create2, name='comment_create2'),
    path('content-let/letbuy/<int:product_id>/comment/', views.comment_create3, name='comment_create3'),

    path('content-neck/neckbuy/comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('content-neck/neckbuy/comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),

    path('content-ear/earbuy/comment/update/<int:comment_id>/', views.comment2_update, name='comment2_update'),
    path('content-ear/earbuy/comment/delete/<int:comment_id>/', views.comment2_delete, name='comment2_delete'),

    path('content-let/letbuy/comment/update/<int:comment_id>/', views.comment3_update, name='comment3_update'),
    path('content-let/letbuy/comment/delete/<int:comment_id>/', views.comment3_delete, name='comment3_delete'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)