from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from shop.cart import Cart
from .forms import ReviewForm, RegistrationForm, LoginForm, CartAddForm
from .models import Product, Review, Category


def get_session_id(request):
    if not request.user.is_authenticated:
        user_session = request.session.session_key
        if not user_session:
            user_session = request.session.cycle_key()
    else:
        user_session = request.user.username
    return user_session


def base_view(request):
    template = "shop/main.html"
    products = Product.objects.all()
    categories = Category.objects.all()
    cart = Cart(request)
    cart_len = len(cart)
    context = {'products': products,
               'categories': categories,
               'cart_len': cart_len, }

    return render(request, template, context)


def category_view(request, slug):
    template = "shop/category.html"
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    category_slug = slug
    products = category.products.all()
    cart = Cart(request)
    current_page = request.GET.get('page', 1)
    paginator = Paginator(products, 3)
    page_items = paginator.get_page(current_page)
    prev_page_url = None
    next_page_url = None
    if page_items.has_next():
        next_page_url = page_items.next_page_number()
    if page_items.has_previous():
        prev_page_url = page_items.previous_page_number()
    context = {
        'category': category,
        'categories': categories,
        'category_slug': category_slug,
        'cart_len': len(cart),
        'products': products,
        'page': current_page,
        'page_items': page_items,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    }
    return render(request, template, context)


def object_view(request, category_name, slug):
    user_session = request.session.session_key
    template = "shop/shop_item.html"
    product = get_object_or_404(Product, slug=slug)
    form = ReviewForm()
    identifier = product.id
    reviews = Review.objects.filter(item=product.id).order_by('-timestamp')
    categories = Category.objects.all()
    cart_product_form = CartAddForm()
    cart = Cart(request)
    context = {
        'item': product,
        'reviews': reviews,
        'identifier': identifier,
        'form': form,
        'categories': categories,
        'cat_name': category_name,
        'slug': slug,
        'cart_product_form': cart_product_form,
        'cart_len': len(cart)
    }
    for review in reviews:
        if review.session == user_session:
            context["reviewed"] = True
            break
    if not user_session:
        request.session.cycle_key()
        user_session = request.session.session_key
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(item=Product.objects.get(id=identifier),
                                  name=form.cleaned_data.get('name'),
                                  text=form.cleaned_data.get('text'),
                                  rating=form.cleaned_data.get('stars'),
                                  session=user_session
                                  )
            return redirect('object_view', category_name=category_name, slug=slug)
    return render(request, template, context)


def cart_clear(request):
    cart = Cart(request)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cart.clear()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    form = CartAddForm(request.POST)
    product = (get_object_or_404(Product, id=product_id))
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=cd['update'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@require_POST
def delete_item(request, product_id):
    cart = Cart(request)
    form = CartAddForm(request.POST)
    product = (get_object_or_404(Product, id=product_id))
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=-1,
                 update_quantity=cd['update'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    form = CartAddForm(request.POST)
    product = get_object_or_404(Product, id=product_id)
    if form.is_valid():
        cart.remove(product=product)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_view(request):
    template = "shop/cart.html"
    cart = Cart(request).__repr__()
    categories = Category.objects.all
    products_in_cart = dict()
    products = Product.objects.all()
    for obj in products:
        if str(obj.id) in cart:
            products_in_cart[obj.id] = {'name': obj.name,
                                        'description': obj.description,
                                        'quantity': cart[str(obj.id)]['quantity']}
    context = {'cart': cart,
               'products_in_cart': products_in_cart,
               'cart_len': len(Cart(request)),
               'products': products,
               'categories':categories}

    return render(request, template, context)


def registration_view(request):
    template = "shop/registration.html"
    reg_form = RegistrationForm()
    context = {'user_form': reg_form}
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            new_user = reg_form.save(commit=False)
            new_user.set_password(reg_form.cleaned_data['password2'])
            new_user.save(messages.success(request, ''))
            return render(request, "shop/registration_done.html")
        else:
            messages.error(request, message="Пароли не совпадают!")
    return render(request, template, context)


def login_view(request):
    login_form = LoginForm()
    context = {'login_form': login_form}
    template = "shop/login.html"
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.info(request, 'Неверные логин или пароль!')
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def order_failed(request):
    template = "shop/empty_section.html"
    categories = Category.objects.all()
    return render(request, template, {'categories': categories,
                                      'cart_len': len(Cart(request))})