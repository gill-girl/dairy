from django.shortcuts import render, get_object_or_404,redirect
from menus.models import Product
from .models import Cart, CartItem
from orders .models import Order
from django.views.decorators.http import require_POST
from django.http import JsonResponse

@require_POST


def cart_add(request, product_id):
    cart_id = request.session.get('cart_id')

    # Get or create cart
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    # Get productro
    product = get_object_or_404(Product,id=product_id)
    

    # Create or update cart item
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    response_data = {
        'success': True,
        'message': f'Added {product.name} to cart'
    }

    return JsonResponse(response_data)


def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)
    if not cart  or not cart.items.exists():
         cart=None
    

    return render(request, 'cart/detail.html', {'cart': cart})

def cart_view(request):
    # Get cart ID from session
    cart_id = request.session.get('cart_id')
    if not cart_id:
        # No cart yet, maybe redirect to product list or empty cart page
        return render(request, 'cart/view.html', {'cart': None})

    cart = get_object_or_404(Cart, id=cart_id)

    return render(request, 'cart/view.html', {'cart': cart})

    
    















  
def cart_remove(request, item_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(CartItem, id=item_id, cart=cart)
    item.delete()
    return redirect('cart:cart_detail')


