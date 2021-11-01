from django.urls import path
from .views import BillListView
from . import views

urlpatterns = [
    path('', BillListView.as_view(), name='billing-home'),
    path('about/', views.about, name='billing-about'),
]

