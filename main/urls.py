from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout/', views.checkout, name='checkout'),
    path('about/', views.about, name='about'),
    path('create_order/', views.create_order, name='create_order'),
]