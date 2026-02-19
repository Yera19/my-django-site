from django.shortcuts import render
from .models import Product

def index(request):
    category_name = request.GET.get('category')
    if category_name:
        products = Product.objects.filter(category=category_name)
    else:
        products = Product.objects.all()
    
    categories = ["Смартфоны", "Ноутбуки", "Наушники"]
    return render(request, 'main/index.html', {
        'products': products, 
        'categories': categories
    })

def checkout(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/index.html')

def create_order(request):
    # Эта функция нужна, чтобы работала отправка заказа
    return render(request, 'main/index.html')
    
