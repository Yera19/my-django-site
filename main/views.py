from django.shortcuts import render
from .models import Product

def index(request):
    category_name = request.GET.get('category')
    if category_name:
        products = Product.objects.filter(category=category_name)
    else:
        products = Product.objects.all()
    
    # Список категорий для кнопок
    categories = ["Смартфоны", "Ноутбуки", "Наушники"]
    
    return render(request, 'main/index.html', {
        'products': products,
        'categories': categories
    })

# Функция для страницы оформления (чтобы не было ошибки)
def checkout(request):
    return render(request, 'main/index.html')

# Функция для страницы "О нас" / Контакты (её просит твой urls.py)
def about(request):
    return render(request, 'main/index.html')
    
