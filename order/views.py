from django.shortcuts import render, get_object_or_404

# Create your views here.
from order.forms import OrderCreateForm
from order.models import OrderItem
from shop.cart import Cart
from shop.models import Product


def order_create_view(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    cartobj = cart.__repr__()

    template = 'order/order_creation.html'
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cartobj:
                product = get_object_or_404(Product, id=item)
                OrderItem.objects.create(order=order,
                                         product=product,
                                         price=cartobj[item]['price'],
                                         quantity=cartobj[item]['quantity'])
            cart.clear()
            return render(request, 'order/order_created.html', {'order': order})
        else:
            return render(request, template, {'form': form, 'cart': cartobj, 'cart_len': len(cart),
                                              'total_price': total_price})
    else:
        form = OrderCreateForm
        return render(request, template, {'form': form, 'cart': cart})


def order_created_view(request):
    template = 'order/order_created.html'
    context ={}
    return render(request, template, context)