from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^resources/', include('resources.urls')),
    url(r'^servicedesk/', include('servicedesk.urls')),
]
