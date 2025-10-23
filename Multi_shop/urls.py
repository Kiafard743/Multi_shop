from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Multi_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('account.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('api/', include('products.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
