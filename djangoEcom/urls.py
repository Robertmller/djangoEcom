from django.contrib import admin
from django.urls import path, include
from djangoEcomApp import views, urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoEcomApp.urls')),
]
