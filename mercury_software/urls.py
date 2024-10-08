from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),  # Core uygulamasının URL'leri
    path('blog/', include('blog.urls')),  # Blog uygulamasının URL'leri
    path('startups/', include('startups.urls')),  # Startuplar uygulamasının URL'leri
    path('admin/', admin.site.urls),  # Django admin paneli
]