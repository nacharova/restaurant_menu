from django.shortcuts import render
from .models import Dish
from .forms import DishForm
from .serializers import DishSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


# главная (список блюд)
def index(request):
    dishes = Dish.objects.all()
    return render(request, 'restaurant_menu/index.html', {'dishes': dishes, })


# обработка заказа
def order(request):
    dishes = Dish.objects.all()
    if request.method == 'POST':
        checked_dishes = list()
        total_price = 0
        for dish in dishes:
            dish_is_checked = dishes.filter(pk__in=request.POST.get("check_{id}".format(id=dish.id), ()))
            if dish_is_checked:
                for item in dish_is_checked:
                    total_price += item.price
                checked_dishes.append(dish_is_checked)
        print(checked_dishes)
        if not checked_dishes:
            return render(request, 'restaurant_menu/index.html', {
                'error_message': "Не выбрано ни одно блюдо.", 'dishes': dishes,
            })
        return render(request, 'restaurant_menu/order.html',
                      {'checked_dishes': checked_dishes, 'total_price': total_price})
    return render(request, 'restaurant_menu/index.html', {'dishes': dishes})


# добавление нового блюда
def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'restaurant_menu/add_dish.html', {'form_saved': "Блюдо успешно добавлено"})
        else:
            return render(request, 'restaurant_menu/add_dish.html', {'form': form})
    else:
        form = DishForm()
    return render(request, 'restaurant_menu/add_dish.html', {'form': form})


@csrf_exempt
def api(request):
    if request.method == 'GET':
        dishes = Dish.objects.all()
        serializer = DishSerializer(dishes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DishSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)