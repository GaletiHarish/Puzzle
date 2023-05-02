from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('softskilldetectiveapp.urls')),
    path('admin/', admin.site.urls),
    path('puzzle/', include('puzzle.urls')),
]
