from django import forms
from .models import Dish


class DishForm(forms.ModelForm):
    name = forms.CharField(label='название блюда', max_length=255)
    food_value = forms.IntegerField(label='пищевая ценность')
    price = forms.FloatField(label='цена')
    image = forms.ImageField(label='картинка', required=False)

    class Meta:
        model = Dish
        fields = "__all__"
