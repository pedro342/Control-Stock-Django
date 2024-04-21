from django.urls import path
from . import views

urlpatterns = [
    #vistas que vaya creando path('/', views.miVista, name='nombreVista'),
    path('register-form/', views.register_form, name='register_form'),
    path('login-form/', views.login_form, name='login_form'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register-products/', views.register_products, name='registerProducts'),
    path('register-products-form/', views.registerProducts_form, name='registerProducts_form'),
    path('search-products/', views.search_products, name='search_products'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='productUpdate'),
    path('product/<int:pk>/delete/', views.ProductoDelete.as_view(), name='productDelete'),
    path('products-table/', views.products_table, name='products_table'),
]