from django.shortcuts import render

'''responder uma requisicao'''

def index(request):
    return render(request, 'galeria/index.html')


def imagem(request):
    return render(request, 'galeria/imagem.html')
