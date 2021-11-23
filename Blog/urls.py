from django.contrib import admin
from django.urls import path, include
from Blog import views

urlpatterns = [
    path('', views.BlogHome, name='BlogHome'),
    path('<str:slug>', views.BlogPost, name='BlogPost'),
]