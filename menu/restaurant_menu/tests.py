from django.test import TestCase
from django.urls import reverse
from .forms import DishForm
from django.core.files.base import ContentFile
from django.conf import settings
import os


class DishModelTests(TestCase):
    def test_response_status(self):
        """Тест на отображение страницы"""
        response = self.client.get(reverse('add_dish'))
        self.assertEqual(response.status_code, 200)

    def test_form_no_image_is_valid(self):
        """Тест на валидацию формы без необязательной картинки"""
        form_data = {'name': 'test', 'food_value': 250, 'price': 300, 'image': None}
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_adding_new_dish(self):
        """Тест на добавление нового блюда"""

        with open(os.path.join(settings.BASE_DIR, 'restaurant_menu/static/restaurant_menu/r-1.png'), 'rb') as f:
            image_file = ContentFile(f.read(), 'r-1.png')
        form_data = {'name': 'test_form', 'food_value': 250, 'price': 300}
        files = {'image': image_file}
        form = DishForm(form_data, files)
        self.assertTrue(form.is_valid())
        new_dish = form.save()
        # проверка соответствия данных
        for data in form_data:
            self.assertEqual(getattr(new_dish, data), form_data[data])
        self.assertIsNotNone(new_dish.image)
        # проверка, что файл сохранился
        self.assertTrue(os.path.exists(new_dish.image.path))
