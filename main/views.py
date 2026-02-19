from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, OrderRequest
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    category_name = request.GET.get('category')
    if category_name:
        products = Product.objects.filter(category=category_name)
    else:
        products = Product.objects.all()
    categories = ["Смартфоны", "Ноутбуки", "Наушники"]
    return render(request, 'main/index.html', {'products': products, 'categories': categories})

def about(request):
    # Здесь должен открываться твой файл с информацией об авторе
    return render(request, 'main/about.html')

def checkout(request):
    # Здесь должен открываться твой файл оформления заказа
    return render(request, 'main/checkout.html')

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        OrderRequest.objects.create(
            client_name=data.get('name'),
            phone=data.get('phone', 'Не указан'),
            product_list=data.get('products'),
            total_price=data.get('total'),
            method=data.get('method'),
            term=int(data.get('term', 0))
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'}, status=400)
    
