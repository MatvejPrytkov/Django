from django.http import HttpResponse
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]

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
    try:
        item = Item.objects.get(id=number)
    except ObjectDoesNotExist:
        return render(request, "errors.html", """Товар с id ={number} не найден""")
    # response = next((item for item in items if item['id'] == number), None)  
    # if response is None:
    #     return HttpResponse("Товар не найден")  
    # response_text = "<br>".join([f"{key}: {value}" for key, value in response.items()])  
    # return HttpResponse(response_text)
     # f"""<h2> Имя: {item["name"]}</h2>
            # <p> Количество: {item["quantity"]}</p>
            # <p> <a href = "/items"> Назад к списку товаров </a> </p> """
    else:
        context = {"item":item}
            # {
            #     "name":item['name'],
            #     "quantity": item['quantity']
            # }
        return render(request, "item.html", context)
    

def goods(request):
    # response_html = "<h1> Список товаров</h1><ol>" 
    # for item in items:
    #     response_html += f"<li> <a href='/item/{item['id']}'>{item['name']} </li>"
    # response_html += "</ol>"  
    # return render(request,"items.html", response_html)
    context = {
        "items": Item.objects.all()
    }
    return render(request, "items.html", context)

        


