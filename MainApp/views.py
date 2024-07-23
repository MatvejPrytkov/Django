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
    context = {
        "name": "Прытков Матвей Павлович",
        "email":"email@mail.ru"
    }
    return render(request, "index.html", context)
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
    # response = next((item for item in items if item['id'] == number), None)  
    # if response is None:
    #     return HttpResponse("Товар не найден")  
    # response_text = "<br>".join([f"{key}: {value}" for key, value in response.items()])  
    # return HttpResponse(response_text)  
    for item in items:
        if item['id']==number:
            result = f"""<h2> Имя: {item["name"]}</h2>
            <p> Количество: {item["quantity"]}</p>
            <p> <a href = "/items"> Назад к списку товаров </a> </p> """
            return HttpResponse(result)
    return HttpResponse(f"""Товар с id ={number} не найден""")
def goods(request):
    response_html = "<h1> Список товаров</h1><ul>" 
    for item in items:
        response_html += f"<li> <a href='/item/{item['id']}'>{item['name']} </li>"
    response_html += "</ul>"  
    return HttpResponse(response_html)
    

        


