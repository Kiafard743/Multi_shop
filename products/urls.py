from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='detail'),
    path('navbar/', views.NavbarPartialView.as_view(), name='navbar'),
    path('all/', views.ProductsListView.as_view(), name='products_list'),
]