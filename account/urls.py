from django.contrib.auth.views import LogoutView
from django.urls import path

from account import views
from account.views import RegisterView, VerifyCode, CustomLoginView

app_name = 'account'
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', VerifyCode.as_view(), name='verifycode'),
    path('logout/', LogoutView.as_view(next_page='home:home'), name='logout'),
    path('add_address/', views.AddAddressView.as_view(), name='add_address'),
]