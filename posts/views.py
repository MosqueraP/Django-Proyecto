from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import datetime
from django.views import View # vistas basadas en clase

# Create your views here.

def dummy_view(request, id):
    return render(request, 'posts/posts_ist.html')

def status_code_view(request):
    return HttpResponseNotFound('Pagina web no envontrada, error 404')


def entry_list(request):
    return render(request, 'posts/entry_list.html')


def redirect_back_home(request):
    return redirect('hhtp://google.com')

class MyClassView(View):
    def get(self, request):
        print('Correr codigo')
        return HttpResponse('Desde una vista CBV, vista basada en clases')
        



