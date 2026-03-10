from django.urls import path
from galeria.views import index, imagem

'''Lista para manter as rotas da aplicacao'''

urlpatterns = [
    path('', index),
    path('imagem/', imagem, name='imagem')
]