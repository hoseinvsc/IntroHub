from django.shortcuts import render
from .models import Customer, Product

def home(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    print(products)
    context = {'products': products,"customers":customers}
    return render(request, 'home.html', context)

def product_detail(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request, 'product_detail.html', {'product': product})

def about(request):
    return render(request, 'about.html')

def connect(request):
    return render(request, 'connect.html')

def product(request):
    return render(request, 'product.html')
