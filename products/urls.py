from django.urls import path
from rest_framework import routers

from products import views
from products.api_views import ProductViewSet

app_name = 'products'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='detail'),
    path('navbar/', views.NavbarPartialView.as_view(), name='navbar'),
    path('all/', views.ProductsListView.as_view(), name='products_list'),
] + router.urls