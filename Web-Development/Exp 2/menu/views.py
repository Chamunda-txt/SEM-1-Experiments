
from django.shortcuts import render
from .models import FoodItem


def food_list(request):
    foods = FoodItem.objects.all()

    return render(request, 'menu/food_list.html', {
        'foods': foods
    })
