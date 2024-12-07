from django.shortcuts import render
from .models import Product, Category
# Create your views here.
def home(request):
    return render(request, "base.html")

   
    
    
    