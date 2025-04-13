from django.shortcuts import render,get_object_or_404
from .models import Customer, Product , Blog

def home(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    print(products)
    context = {'products': products,"customers":customers}
    return render(request, 'home.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products.html', {'products': all_products})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def blog(request):
    posts = Blog.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'post': post})
