from django.db import models



class Product(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название товара")

    price = models.IntegerField(verbose_name="Цена (₸)")

    image_url = models.URLField(verbose_name="Ссылка на фото")

    # Обычное текстовое поле для категорий

    category = models.CharField(max_length=100, verbose_name="Категория", default="Смартфоны")



    class Meta:

        verbose_name = "Товар"

        verbose_name_plural = "Товары"



    def __str__(self):

        return self.name



class OrderRequest(models.Model):

    client_name = models.CharField(max_length=100, verbose_name="Имя клиента")

    phone = models.CharField(max_length=20, verbose_name="WhatsApp номер")

    product_list = models.TextField(verbose_name="Список товаров")

    total_price = models.CharField(max_length=50, verbose_name="Сумма")

    method = models.CharField(max_length=50, verbose_name="Способ оплаты")

    term = models.IntegerField(verbose_name="Срок (мес.)", default=0)

    status = models.CharField(max_length=20, default="Новый", verbose_name="Статус")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")



    class Meta:

        verbose_name = "Заявка"

        verbose_name_plural = "Заявки"



    def __str__(self):

        return f"{self.client_name} - {self.method}"

        
