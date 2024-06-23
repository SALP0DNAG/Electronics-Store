from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:category_name>/', views.category, name='category'),
    path('all_categories/', views.category_all, name='category_all'),
    path('compares/', views.compares, name='compares'),
    path('favorites/', views.favorites, name='favorites'),
    path('basket/', views.basket, name='basket'),
    path('basket-add/<int:product_id>', views.basket_add, name='basket_add'),
    path('basket-minus/<int:basket_id>', views.basket_minus, name='basket_minus'),
    path('basket-delete/<int:basket_id>', views.basket_delete, name='basket_delete'),
]
