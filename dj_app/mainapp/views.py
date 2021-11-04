from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404
import random


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


links_menu = [
    {'url': 'products_all',
        'title': 'Все'
     },
    {'url': 'products_home',
        'title': 'Продукты для дома'
     },
    {'url': 'products_office',
        'title': 'для офиса'
     },
    {'url': 'products_modern',
        'title': 'продукты модерн'
     },
    {'url': 'products_classic',
        'title': 'Классические'
     }
]


def products(request):

    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=content)


def products_home(request):

    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=content)

def products_office(request):

    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=content)

def products_modern(request):

    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=content)

def products_classic(request):

    content = {
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=content)


def main(request):
    title = 'главная'
    
    products = Product.objects.all()[:4]
        
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)

def products(request, pk=None):
    print(pk)
    
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
            
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products_list.html', content)

    
    same_products = Product.objects.all()[3:5]
    
    content = {
        'title': title, 
        'links_menu': links_menu, 
        'same_products': same_products
    }
    
    return render(request, 'mainapp/products.html', content)
basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
            
    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')
        
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }
        
        return render(request, 'mainapp/products_list.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

        
def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]
    
    
def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).\
                                    exclude(pk=hot_product.pk)[:3]

    return same_products
   
def products(request, pk=None):   
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)
           
    ...
    
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    
    content = {
        'title': title,
        'links_menu': links_menu, 
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }
    
    return render(request, 'mainapp/products.html', content)

def product(request, pk):
    title = 'продукты'
    
    content = {
        'title': title, 
        'links_menu': ProductCategory.objects.all(), 
        'product': get_object_or_404(Product, pk=pk), 
        'basket': get_basket(request.user),
    }
	
    return render(request, 'mainapp/product.html', content)