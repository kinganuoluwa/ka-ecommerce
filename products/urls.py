from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('create/', views.product_create, name='create'),
    path('<str:slug>/', views.product_detail, name='detail'),
    path('<str:slug>/update/', views.product_update, name='update'),
    path('<str:slug>/delete/', views.product_delete, name='delete'),
]
