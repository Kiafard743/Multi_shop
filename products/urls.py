from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('detail/<int:pk>', views.ProductDetailView.as_view(), name='detail'),
]