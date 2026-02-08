from django.contrib import admin
from .models import Product, OrderRequest

admin.site.register(Product)

@admin.register(OrderRequest)
class OrderRequestAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'phone', 'method', 'term', 'total_price', 'status', 'created_at')
    list_filter = ('method', 'status')
    actions = ['approve']

    def approve(self, request, queryset):
        queryset.update(status='Одобрено')
    approve.short_description = "✅ Одобрить заказ"