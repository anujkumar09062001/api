from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from api.views import StudentView
from rest_framework import routers

route = routers.DefaultRouter()
route.register("", StudentView, basename='studentview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
]
