from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

import datetime
from django.views import View # vistas basadas en clase
from django.views.generic import ListView # lista de objetos en set
from .models import Entry

# Create your views here.

def dummy_view(request):
    return render(request, 'posts/posts_list.html', {})

def status_code_view(request):
    return HttpResponseNotFound('Pagina web no envontrada, error 404', {})


def entry_list(request):
    return render(request, 'posts/posts_list.html', {})


def redirect_back_home(request):
    return redirect('hhtp://google.com')

class MyClassView(View):
    def get(self, request):
        print('Correr codigo')
        return HttpResponse('Desde una vista CBV, vista basada en clases')
        

class MyLisView(ListView):
        model = Entry



