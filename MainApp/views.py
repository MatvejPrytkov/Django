from django.http import HttpResponse
from django.shortcuts import render
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    text = """<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>Прытков М. П.</i>
"""
    return HttpResponse (text)
def dosie(request):
    name = 'Matvej'
    surname = 'Prytkov'
    otch = 'Pavlovich'
    phone = '+79221223171'
    email = 'prytkovmatvej@bk.ru'
    text = {'Имя ': name, 'Отчество ': otch, 'Фамилия ': surname, 'Телефон ': phone, 'Почта ': email}
    response_text = "<br>".join([f"{key}: {value}" for key, value in text.items()])
    return HttpResponse (response_text)
def item(request, number):
    response = next((item for item in items if item['id'] == number), None)  
    if response is None:
        return HttpResponse("Товар не найден")  
    response_text = "<br>".join([f"{key}: {value}" for key, value in response.items()])  
    return HttpResponse(response_text)  

