from django.shortcuts import render
from .models import Product

def index(request):
    category_name = request.GET.get('category')
    
    if category_name:
        # Фильтруем просто по тексту, который ты ввел в админке
        products = Product.objects.filter(category=category_name)
    else:
        products = Product.objects.all()
    
    # Список категорий для кнопок пропишем вручную здесь, чтобы не создавать таблицы
    categories = ["Смартфоны", "Ноутбуки", "Наушники"]
    
    return render(request, 'main/index.html', {
        'products': products,
        'categories': categories
    })
    
