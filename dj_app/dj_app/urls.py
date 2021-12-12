"""dj_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as mainapp
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import re_path




urlpatterns = [
    path('control/', admin.site.urls),
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'^products/', include('mainapp.urls', namespace='products')),
    path('contact/', mainapp.contact, name='contact'),
    path('products/home/', mainapp.products_home, name='products_home'),
    path('products/office/', mainapp.products_office, name='products_office'),
    path('products/modern/', mainapp.products_modern, name='products_modern'),
    path('products/classic/', mainapp.products_classic, name='products_classic'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('admin/', include('adminapp.urls', namespace='adminapp')),
    path('', include('social_django.urls', namespace='social')),
    re_path(r'^order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
   import debug_toolbar

   urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
