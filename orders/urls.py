from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('new_order/', views.new_order, name='new_order'),
    path('<str:order_id>/', views.order, name='order'),
]
