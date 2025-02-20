from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Category(models.Model):
    name = models.CharField("Названия",max_length=100)
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField("Названия",max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="Категория")
    description = models.CharField("Описание",max_length=300)    
    count = models.PositiveSmallIntegerField("Количество на текущий момент",default=0)
    total_count = models.PositiveBigIntegerField("Общая количество", default=0)
    average_price = models.FloatField("Средняя цена", default=0)
    in_stock = models.CharField("В наличии", default="Нет", max_length=3, choices=(("Да","Да"),("Нет","Нет")))
    created_at = models.DateTimeField("Дата",auto_now_add=True)
    amount_of_transaction = models.PositiveSmallIntegerField("Количество транзакций", default=0)
    is_published = models.CharField("Опубликовано", default="Нет", max_length=3, choices=(("Да","Да"),("Нет","Нет")))
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "Продукты"

class ProductPhoto(models.Model):
    image = models.ImageField("Фотография",upload_to="product", blank=True, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="Продукт")
    
    def __str__(self):
        return f"Фотография:{self.id} "

class Transaction(models.Model):
    COMING = "Приход"
    LEAVING = "Уход"
    ACTION = [
        (COMING,'Приход'),
        (LEAVING,'Уход'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт")
    action = models.CharField("Действие",max_length=10, choices=ACTION)
    count = models.PositiveSmallIntegerField("Количество",default=0)
    price = models.FloatField("Цена")
    created_at = models.DateTimeField("Дата",auto_now_add=True)
    
    def __str__(self):
        return f"{self.action} {self.product.name}, количество: {self.count}, цена: {self.price}"

    class Meta:
        verbose_name = "транзакция"
        verbose_name_plural = "Транзакции"

@receiver(post_save, sender=Transaction)
def update_product_total_count(sender, instance, **kwargs):    
    product = instance.product
    
    #Пересчёт общего количества:  
    transactions = Transaction.objects.filter(product = product)
    
    product.average_price = 0
    product.count = 0 
    product.total_count = 0 
    product.amount_of_transaction = 0  
    for transaction in transactions:       
        
        if transaction.action == transaction.COMING:
            product.average_price += transaction.price * transaction.count 
            product.total_count += transaction.count
            product.count += transaction.count
            
        if transaction.action == transaction.LEAVING:
            product.count -= transaction.count
            product.amount_of_transaction += 1     

    product.average_price /= product.total_count 
    product.average_price = round(product.average_price) 
    if product.count > 0:
        product.in_stock = "Да"
    else:
        product.in_stock = "Нет"
        
    product.save() 
    
    