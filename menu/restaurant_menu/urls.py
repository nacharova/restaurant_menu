from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.order, name='order'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('api/', views.api, name='api')
]
