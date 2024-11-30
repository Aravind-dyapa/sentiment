from django.contrib import admin
from django.urls import path, include  # Include is used to route to app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),   # Admin route
    path('', include('sentiment_app.urls')),  # Route to the sentiment_app's URLs
]
