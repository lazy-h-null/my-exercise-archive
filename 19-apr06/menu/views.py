from django.shortcuts import render
from .models import Dish
# Create your views here.

def menu_view(request):
    all_dishes = Dish.objects.all()
    return render(request, 'menu.html', {'menu_items': all_dishes})