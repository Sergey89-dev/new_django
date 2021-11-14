from django.urls import path
import mainapp.views as mainapp

from django.urls import path

import mainapp.views as mainapp
from django.urls import path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
]



import mainapp.views as mainapp
app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('<int:pk>/', mainapp.products, name='category')
]

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('category/<int:pk>/', mainapp.products, name='category'),
    path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
