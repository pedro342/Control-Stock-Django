from django.shortcuts import render, redirect
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import User, Products
from .forms import ProductForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create(username=username, password=password)
        return JsonResponse({'message':'The user was create successfully'})
    else:
        return JsonResponse({'message':'Method not allowed'}, status=405)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).exists()
        if user:
            return registerProducts_form(request)
        else:
            return JsonResponse({'message':'Username or password incorrect'})
    else:
        return JsonResponse({'messagge':'Method not allowed'}, status=405)

def register_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(registerProducts_form)
    else:
        form = ProductForm()
    return render(request, 'registerProducts.html', {'form': form})

def search_products(request):
    if 'query' in request.GET:
        query = request.GET['query']
        nameProduct = Products.objects.filter(nameProduct__icontains=query)
        return render(request, 'findProducts.html', {'nameProduct':nameProduct, 'query':query})
    else:
        return render(request, 'findProducts.html')
    
class ProductUpdate(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'updateProducts.html'
    success_url = reverse_lazy('search_products')

class ProductoDelete(DeleteView):
    model = Products
    success_url = reverse_lazy('search_products')
    
def register_form(request):
    return render(request, 'register.html')

def login_form(request):
    return render(request, 'login.html')

def registerProducts_form(request):
    return render(request, 'registerProducts.html')