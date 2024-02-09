from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('orders/', views.orders, name='orders'),
    path('address/', views.address, name='address'),
    path('discounts-and-bonuses/', views.discounts_and_bonuses, name='discounts-and-bonuses'),
    path('contacts/', views.contacts, name='contacts'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
