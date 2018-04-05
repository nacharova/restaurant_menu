from django import forms


class DishForm(forms.Form):
    check = forms.CheckboxSelectMultiple()
    name = forms.CharField(label='название блюда', max_length=255)
    food_value = forms.IntegerField(label='пищевая ценность')
    price = forms.FloatField(label='цена')
    image = forms.ImageField(label='картинка', required=False)