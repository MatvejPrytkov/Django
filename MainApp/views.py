from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    text = """<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>Прытков М. П.</i>
"""
    return HttpResponse (text)
def dosie(request):
    name = 'Matvej',
    surname = 'Prytkov',
    otch = 'Pavlovich',
    phone = '+79221223171'
    email = 'prytkovmatvej@bk.ru'
    text = {'Имя': name, 'Отчество': otch, 'Фамилия': surname, 'Телефон': phone, 'Почта': email}
    return HttpResponse (text)

# Create your views here.
