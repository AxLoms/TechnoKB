from django.contrib import admin
from product.models import Category,Product,Transaction,ProductPhoto
from mptt.admin import MPTTModelAdmin,TreeRelatedFieldListFilter
# Register your models here.

admin.site.site_header = 'Администрация TechnoKB'
admin.site.index_title = 'Наши модели'
admin.site.site_title = 'Продукты - Административная панель'

class TransactionAdmin(admin.TabularInline):
    model = Transaction
    list_display = ('created_at',)
    readonly_fields = ('created_at',)  
    extra = 1  

class AdminPhoto(admin.TabularInline):
    model = ProductPhoto
    extra = 1


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('name','parent')
    list_filter = (('parent', admin.RelatedFieldListFilter),)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    
    inlines = [AdminPhoto,TransactionAdmin]    
    list_display = ('name','category','count','in_stock','is_published','created_at','amount_of_transaction',)
    search_fields = ('name',)
    list_filter = (('category',TreeRelatedFieldListFilter),'in_stock',)    
    ordering = ('name',)
    readonly_fields = ('count','average_price','total_count','in_stock','created_at','amount_of_transaction',)
    autocomplete_fields = ('category',) 

    class Meta:
        model = Product
       



admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)


