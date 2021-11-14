from django.urls import path
from adminapp import views as admin_views
app_name = 'admin_views'

urlpatterns = [
    path('users/create/', admin_views.user_create, name='user_create'),
    path('users/read/', admin_views.users, name='users'),
    path('users/update/<int:pk>/', admin_views.user_update, name='user_update'),
    path('users/delete/<int:pk>/', admin_views.user_delete, name='user_delete'),
    path('categories/create/', admin_views.category_create, name='category_create'),
    path('categories/read/', admin_views.categories, name='categories'),
    path('categories/update/<int:pk>/',admin_views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/',admin_views.category_delete, name='category_delete'),
    path('products/create/category/<int:pk>/', admin_views.product_create, name='product_create'),
    path('products/read/category/<int:pk>/',admin_views.products, name='products'),
    path('products/read/<int:pk>/', admin_views.product_read, name='product_read'),
    path('products/update/<int:pk>/',admin_views.product_update, name='product_update'),
    path('products/delete/<int:pk>/',admin_views.product_delete, name='product_delete'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users')

]
