from django.urls import path
from .views import ProductListView, ProductSearchView, ProductSelectView, DashboardView, login_view

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('products/select/<int:pk>/', ProductSelectView.as_view(), name='product-select'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/', login_view, name='login'),
]
