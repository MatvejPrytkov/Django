from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    text = """<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>Прытков М. П.</i>
"""
    return HttpResponse (text)
# Create your views here.
