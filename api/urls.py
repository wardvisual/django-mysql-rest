from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('product-list/', views.show_all, name='product-list'),
    path('product/<int:pk>', views.view_product, name='product'),
    path('product-create', views.create_product, name='product-create'),
    path('product-update/<int:pk>/', views.update_product, name='product-update'),
    path('product-delete/<int:pk>/', views.delete_product, name='product-delete'),
]