from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages



def home(request):
    featured_products = Product.objects.filter(is_featured=True)
    return render(request, 'store/index.html', {'featured_products': featured_products})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login (request, user)
            return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "store/register.html",  {"form" : form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
        else:
            messages.error(request, 'User not found.')

    return render(request, 'store/login.html', {'form': AuthenticationForm()})

def user_logout(request):
    logout(request)
    return redirect('home')

def search(request):
    query = request.GET.get('q', '')
    results = Product.objects.filter(name__icontains=query) if query else None
    return render(request, 'store/search_results.html', {'results': results, 'query': query})


def shop(request):
    products = Product.objects.all()
    return render(request, 'store/shop.html', {'products' : products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity+=1
        cart_item.save()

    return redirect('cart')

def cart_view(request):
    
    cart_items = Cart.objects.filter(user=request.user)

    
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

def remove_from_cart(request, item_id):
    try:
        item = Cart.objects.get(id=item_id, user=request.user)
        item.delete()
    except Cart.DoesNotExist:
        pass
    return redirect('cart')