from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URL patterns from the contacts app
    path('', include('contacts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
