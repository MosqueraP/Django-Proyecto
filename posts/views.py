from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
import datetime
from django.views import View # vistas basadas en clase

# Create your views here.

def dummy_view(request, id):
    now = datetime.datetime.now()
    html = f'''<html>
                <body>
                    <h1>Hola mundo</h1>
                    <p>La fecha actual es:</p>
                        <p>Fecha Hoy: {now}</p>
                        <p>id: {id}</p>
                    </body>
                </html>'''
    return HttpResponse(html)

def status_code_view(request):
    return HttpResponseNotFound('Pagina web no envontrada, error 404')


def entry_list(request):
    return render(request, 'posts/entry_list.html')


def redirect_back_home(request):
    return redirect('hhtp://google.com')


