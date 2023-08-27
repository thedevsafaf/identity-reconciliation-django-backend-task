from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URL patterns from the contacts app
    path('', include('contacts.urls')),
]
