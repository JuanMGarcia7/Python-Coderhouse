from django.shortcuts import render

# Create your views here.
from Products.models import Products

def create_product(request):
    new_product = Products.objects.create(name="Mouse Logitech" , price= 14600 , stock=True)
    print(new_product)
    return render(request, 'create-product.html', context={})

def list_products(request):
    list_of_products = Products.objects.all()
    context={
        "list_of_products": list_of_products
    }
    return render (request, 'list_prod.html', context=context)

