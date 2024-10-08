from django.contrib import admin
from django.urls import path, include
from path import urlsglobal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urlsglobal.estetica)),
    path('login/',include(urlsglobal.usuarios)),
]
