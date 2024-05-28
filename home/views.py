from django.shortcuts import render, redirect
from .models import Product, ProductType
from .forms import RegisterForm
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib import messages



def index(request):
    data = {
        'recommend_products': Product.objects.all(),
        'hot_products': Product.objects.filter(Rating__gte=4, Sold__gte=10)
    }
    return render(request, 'pages/home.html', data);

def menu(request, typeID=None):
    product_types = ProductType.objects.all()
    products = Product.objects.all()

    if typeID:
        products = products.filter(TypeID=typeID)

    data = {
        'product_types': product_types,
        'products': products,
    }
    return render(request, 'pages/menu.html', data)

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        userName = request.POST.get('username')
        passWord = request.POST.get('password')
        user = authenticate(request, username= userName, password= passWord)
        if user is not None:
            login(request,user)
            return redirect('index')
        else: 
            messages.info(request,'user or password not correct!')
            
    return render(request, 'pages/login.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Chuyển hướng đến trang thành công
    else:
        form = RegisterForm()

    return render(request, 'pages/register.html', {'form': form})


