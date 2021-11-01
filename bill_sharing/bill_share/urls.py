from django.urls import path
from .views import (
    BillListView, 
    BillDetailView, 
    BillCreateView, 
    BillUpdateView
    )
from . import views

urlpatterns = [
    path('', BillListView.as_view(), name='billing-home'),
    path('bill/<int:pk>/', BillDetailView.as_view(), name='bill-detail'),
    path('bill/new/', BillCreateView.as_view(), name='bill-create'),
    path('bill/<int:pk>/update', BillUpdateView.as_view(), name='bill-update'),
    path('about/', views.about, name='billing-about'),

]

