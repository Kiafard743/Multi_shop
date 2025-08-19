from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from .views import HomeView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home')
]