from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductListCreateView.as_view(), name='productos-list-create'),
    path('productos/<int:pk>/', views.ProductDetailView.as_view(), name='productos-detail'),
]