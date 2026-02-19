from django.shortcuts import render
from .models import Product

def index(request):
    # Получаем выбранную категорию из ссылки
    category_name = request.GET.get('category')
    
    if category_name:
        # Ищем товары, где в поле category написано это слово
        products = Product.objects.filter(category=category_name)
    else:
        # Если категория не выбрана, показываем всё
        products = Product.objects.all()
    
    # Список категорий для кнопок (должны совпадать с тем, что пишешь в админке)
    categories = ["Смартфоны", "Ноутбуки", "Наушники"]
    
    return render(request, 'main/index.html', {
        'products': products,
        'categories': categories
    })

def checkout(request):
    # Эта функция нужна, чтобы кнопка "Оформить" не вызывала ошибку 500
    # Она просто открывает ту же главную или страницу оформления
    return render(request, 'main/index.html') 
