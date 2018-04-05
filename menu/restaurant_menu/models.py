from django.db import models


class Dish(models.Model):
    name = models.CharField(max_length=255)  # название блюда
    food_value = models.IntegerField()  # пищевая ценность
    price = models.FloatField()  # цена
    image = models.ImageField()  # картиночка

    def __str__(self):
        return self.name
