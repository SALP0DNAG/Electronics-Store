from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_categories/', views.category_all, name='category_all'),
    path('compares/', views.compares, name='compares'),
    path('basket/', views.basket, name='basket'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorites_add/<int:product_id>', views.favorites_add, name='favorites_add'),
    path('favorites_delete/<int:product_id>', views.favorites_delete, name='favorites_delete'),
    path('basket-add/<int:product_id>', views.basket_add, name='basket_add'),
    path('basket-minus/<int:basket_id>', views.basket_minus, name='basket_minus'),
    path('basket-delete/<int:basket_id>', views.basket_delete, name='basket_delete'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('category/<str:category_name>/<int:product_id>', views.product, name='product'),
]
