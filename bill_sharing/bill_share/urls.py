from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='billing-home'),
    path('about/', views.about, name='billing-about'),
    path('login/', views.login, name='billing-login'),
]
