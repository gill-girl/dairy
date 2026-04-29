from django.urls import path
from . import views

app_name = 'menus'

urlpatterns = [
    
    path('', views.product_list, name='product_list'),
    path('products/category/<int:category_id>/', views.product_list, name='product_list'),

    # Category
    path('category/', views.category_list, name='category_list'),
    path('category/<int:id>/', views.category_detail, name='category_detail'),

    
    # Product detail
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
