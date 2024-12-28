from django.shortcuts import render,get_object_or_404
from .models import Product, Category, ProductPhoto
# Create your views here.
def home(request):
    categories = Category.objects.all()   
    
    return render(request, "homepage.html", {"categories": categories})

def products(request):
    # products = Product.objects.all()
    category_id = request.GET.get('category') 
    order = request.GET.get('order')   
    category = "Все категории"
    products = Product.objects.filter(is_publiched = "Да")  
      

    if category_id:
        category = Category.objects.get(id = category_id)
        products = products.filter(category=category_id)


   
        
       
    return render (request, 'products.html', { "products": products, "category": category, "order": order})
    
def product(request,id):
    product = Product.objects.get(id = id)
    images =  ProductPhoto.objects.filter(product = product)
    return render(request, 'product.html', {"product": product, "images": images})






   
    
    
    