from django.shortcuts import render
from .models import Dish
from .forms import DishForm


def index(request):
    form = DishForm
    dishes = Dish.objects.all()
    return render(request, 'restaurant_menu/index.html', {'form': form, 'dishes': dishes,})


def order(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            dishes = Dish.objects.all()
            checked_dishes = dishes.filter(pk__in=request.POST.get('check', ()))
            print(checked_dishes)
            if not checked_dishes:
                return render(request, 'restaurant_menu/index.html', {
                    'error_message': "Не выбрано ни одно блюдо.", 'dishes': dishes,
                })
            return render(request, 'restaurant_menu/order.html', {'checked_dishes': checked_dishes})
