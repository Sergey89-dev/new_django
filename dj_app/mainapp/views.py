from django.shortcuts import render
from .models import ProductCategory, Product
from django.shortcuts import get_object_or_404



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


