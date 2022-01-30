from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from users.views import home, verify

urlpatterns = [
    path('', home, name='home'),
    url(r'^verify/(?P<uuid>[a-z0-9\-]+)/', verify, name='verify'),
    path('admin/', admin.site.urls),
    path('api/v1/', include('backendAPI.urls', namespace='backendAPI')),
]
