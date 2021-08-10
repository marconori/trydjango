from django.shortcuts import render, get_object_or_404

from .forms import ProductForm, RawProductForm

from .models import Product


def product_list_view(request):
    return render("")


def product_create_view(request):
    initial_data = {
        "title": "My favourite title",
        "description": "Insert your description here",
        "price": "100000.00"
    }
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/products_create.html", context)


def product_detail_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    context = {
        "object": obj
    }
    return render(request, "products/products_detail.html", context)


def product_update_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
    context = {
        "object": obj
    }
    return render(request, "products/products_delete.html", context)


def product_delete_view(request, my_id):
    obj = get_object_or_404(Product, id=my_id)
    if request.method == "POST":
        obj.delete()
    context = {
        "object": obj
    }
    return render(request, "products/products_delete.html", context)