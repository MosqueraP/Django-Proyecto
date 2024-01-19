from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import datetime

# Create your views here.

def dummy_view(request):
    now = datetime.datetime.now()
    html = '''<html>
                <body>
                    <h1>Hola mundo</h1>
                    <p>La fecha actual es:</p>
                        <p>{}</p>
                    </body>
                </html>'''.format(now)
    return HttpResponse(html)

def status_code_view(request):
    return HttpResponseNotFound('Pagina web no envontrada, error 404')


def entry_list(request):
    return render(request, 'posts/entry_list.html', {})


