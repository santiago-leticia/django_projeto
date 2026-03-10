from django.contrib import admin
from django.urls import path, include
from galeria.views import index
'''Parte para listar as rotas da aplicacao'''

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]

