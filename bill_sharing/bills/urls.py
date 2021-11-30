from django.urls import path
from .views import (
    BillListView, 
    BillDetailView, 
    BillCreateView, 
    BillUpdateView,
    BillDeleteView
    )
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('', BillListView.as_view(), name='billing-home'),
    path('bill/<int:pk>/', BillDetailView.as_view(), name='bill-detail'),
    path('bill/new/', BillCreateView.as_view(), name='bill-create'),
    path('bill/<int:pk>/update', BillUpdateView.as_view(), name='bill-update'),
    path('bill/<int:pk>/delete', BillDeleteView.as_view(), name='bill-delete'),
    path('about/', views.about, name='billing-about'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
