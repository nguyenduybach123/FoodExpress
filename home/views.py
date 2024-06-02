from django.shortcuts import render, redirect
from .models import Product, ProductType
from .forms import RegisterForm
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib import messages
#cart
from django.shortcuts import get_object_or_404, redirect
from .models import Cart, CartItem



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



def view_cart(request):
    # Lấy giỏ hàng từ session
    cart = request.session.get('cart', {})
    
    # Lấy thông tin sản phẩm từ giỏ hàng
    cart_items = []
    total_price = 0
    for product_id, item in cart.items():
        product = get_object_or_404(Product, ProductID=product_id)
        total_price += product.Price * item['quantity']
        cart_items.append({'product': product, 'quantity': item['quantity']})

    return render(request, 'pages/cart.html', {'cart_items': cart_items, 'total_price': total_price})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Chuyển hướng đến trang thành công
    else:
        form = RegisterForm()

    return render(request, 'pages/register.html', {'form': form})




def add_to_cart(request, product_id):
    product = get_object_or_404(Product, ProductID=product_id)
    
    # Lấy giỏ hàng từ session hoặc tạo mới nếu chưa có
    cart, created = Cart.objects.get_or_create()
    
    # Kiểm tra xem sản phẩm đã có trong giỏ hàng chưa
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')
