from django.shortcuts import render
from .models import Dish
from .forms import DishForm


# главная (список блюд)
def index(request):
    form = DishForm
    dishes = Dish.objects.all()
    return render(request, 'restaurant_menu/index.html', {'form': form, 'dishes': dishes, })


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
    return render(request, 'restaurant_menu/index.html', {'dishes': dishes,
    })


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
