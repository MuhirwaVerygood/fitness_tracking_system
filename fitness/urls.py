from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userapp.urls')),
    path('activities/', include('activityapp.urls')),
]

