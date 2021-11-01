from django.urls import path
from .views import BillListView, BillDetailView, BillCreateView
from . import views

urlpatterns = [
    path('', BillListView.as_view(), name='billing-home'),
    path('bill/<int:pk>/', BillDetailView.as_view(), name='bill-detail'),
    path('bill/new/', BillCreateView.as_view(), name='bill-create'),
    path('about/', views.about, name='billing-about'),

]

