from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreateForm


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products':products})

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product_detail.html', {'product':product})

def product_create(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductCreateForm()
    return render(request, 'products/product_create.html', {'form':form})

def product_update(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')
    else:
        form = ProductCreateForm(instance=product)
    return render(request, 'products/product_update.html', {'form':form})

def product_delete(request, slug):
    product = Product.objects.get(slug=slug)
    product.delete()
    return redirect('products:list')
