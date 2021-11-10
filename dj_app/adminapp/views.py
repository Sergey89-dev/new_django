from django.shortcuts import render

# Create your views here.
from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm



def users(request):
    context = {
        'object_list': ShopUser.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/user.html', context)


def user_create(request):
    context = {

    }
    return render(request, '', context)


def user_update(request, pk):
    context = {

    }
    return render(request, '', context)


def user_delete(request, pk):
    context = {

    }
    return render(request, '', context)


def categories(request):
    context = {
    'object_list': ProductCategory.objects.all().order_by('-is_active')
    }
    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    context = {

    }
    return render(request, '', context)


def category_update(request, pk):
    context = {}
    return render(request, '', context)


def category_delete(request, pk):
    context = {

    }
    return render(request, '', context)


def products(request, pk):
    context = {
    'object_list': Product.objects.filter(category__pk=pk).order_by('-is_active')
    }
    return render(request, 'adminapp/products.html', context)


def product_create(request, pk):
    context = {

    }
    return render(request, '', context)


def product_read(request, pk):
    context = {

    }
    return render(request, '', context)


def product_update(request, pk):
    context = {

    }
    return render(request, '', context)


def product_delete(request, pk):
    context = {

    }
    return render(request, '', context)
@user_passes_test(lambda u: u.is_superuser)
def users(request):
    context = {}
    return render(request, 'adminapp/users.html', context)

def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)   
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()
    
    content = {'title': title, 'update_form': user_form}
    
    return render(request, 'adminapp/user_update.html', content)

def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES,\
                                                        instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update',\
                                                args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)
    
    content = {'title': title, 'update_form': edit_form}
    
    return render(request, 'adminapp/user_update.html', content)
	

def user_delete(request, pk):
    title = 'пользователи/удаление'
    
    user = get_object_or_404(ShopUser, pk=pk)
    
    if request.method == 'POST':
        #user.delete()
        #вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}
    
    return render(request, 'adminapp/user_delete.html', content)


