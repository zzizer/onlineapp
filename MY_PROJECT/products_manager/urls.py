from django.urls import path
from . import views

urlpatterns = [
    path('shopping', views.shopping, name='shopping'),
    path('mycart', views.mycart, name='mycart'),
]
