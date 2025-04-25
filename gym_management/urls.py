from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from gym_management import views
urlpatterns = [
    path('admin/', admin.site.urls),
        path('frontend/', views.frontend_view, name='frontend'),

    path('auth/', include('authentication.urls')), 
    path('classes/', include('classes.urls')),  
    path('booking/', include('booking.urls')), 
    path('membership/', include('membership.urls')), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
