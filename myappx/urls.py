from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings

urlpatterns = [
    path('actual-login/', admin.site.urls),
    path("",home),
    path("index/",home),
    path("about/",about),
    path("services/",services),
    path("emp/",include('emp.urls')),
]
