from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, OrderRequest, Category  # Добавили Category
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    # Получаем ID категории из ссылки (если на неё нажали)
    category_id = request.GET.get('category')
    
    if category_id:
        # Если категория выбрана, фильтруем товары
        products = Product.objects.filter(category_id=category_id)
    else:
        # Если не выбрана — показываем все
        products = Product.objects.all()
    
    # Получаем все категории для меню
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def checkout(request):
    return render(request, 'main/checkout.html')

def about(request):
    return render(request, 'main/about.html')

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            OrderRequest.objects.create(
                client_name=data.get('name'),
                phone=data.get('phone'),
                product_list=data.get('products'),
                total_price=data.get('total'),
                method=data.get('method'),
                term=data.get('term', 0)
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error'}, status=400)
    
