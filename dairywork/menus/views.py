from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Q

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'menus/list.html', {'categories': categories})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    
    return render(request, 'menus/details.html', {'category': category})

def product_list(request, category_id=None):
    category = None
    query = request.GET.get('q')
    products = Product.objects.all()

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'menus/lists.html', {
        'category': category,
        'products': products,
        'query': query,
    })

def product_detail(request, slug, id):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'menus/product_detail.html', {'product': product})
