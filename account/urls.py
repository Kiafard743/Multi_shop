from django.urls import path

from account import views
from account.views import LoginView

app_name = 'account'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('add_address/', views.AddAddressView.as_view(), name='add_address'),
]