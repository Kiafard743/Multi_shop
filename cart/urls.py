from django.urls import path

from cart import views

app_name = 'cart'
urlpatterns = [
    path('cart', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='cart_add'),
    path('delete/<str:id>', views.CartDeleteView.as_view(), name='cart_delete'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/add', views.OrderCreateView.as_view(), name='order_create'),
    path('apply/<int:pk>', views.ApplyDiscountView.as_view(), name='apply_discount'),
]
