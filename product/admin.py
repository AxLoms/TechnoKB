from django.contrib import admin
from .models import Category,Product,Transaction
# Register your models here.

admin.site.site_header = 'Администрация TechnoKB'
admin.site.index_title = 'Наши модели'
admin.site.site_title = 'Продукты - Административная панель'

class TransactionAdmin(admin.TabularInline):
    model = Transaction
    list_display = ('created_at',)
    readonly_fields = ('created_at',)  
    extra = 0  

class ProductAdmin(admin.ModelAdmin):
    inlines = [TransactionAdmin]
    list_display = ('name','category','count','in_stock','is_publiched',)
    search_fields = ('name',)
    list_filter = ('category','in_stock',)    
    ordering = ('name',)
    readonly_fields = ('count','average_price','total_count','in_stock',)

    class Meta:
        model = Product




admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
