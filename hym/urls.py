from django.contrib import admin
from django.urls import path
from hym.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('accesorio/', accesorio),
    path('ropa/', ropa),
	path('imagenes/', imagenes),
]
