from django.urls import path
from . import views

app_name = 'page'

urlpatterns = [
    path('about_us/', views.about_us, name='about_us'),
    path('payment/', views.payment, name='payment'),
    path('delivery/', views.delivery, name='delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.news, name='news'),
    path('requisites/', views.requisites, name='requisites'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('how_to_order/', views.how_to_order, name='how_to_order'),
    path('discounts_and_bonuses/', views.discounts_and_bonuses, name='discounts_and_bonuses'),
    path('return_of_goods/', views.return_of_goods, name='return_of_goods'),
    path('bulk_orders/', views.bulk_orders, name='bulk_orders'),
    path('suppliers/', views.suppliers, name='suppliers'),
]
