from django.shortcuts import render

from .forms import ProductForm

from .models import Product

def product_create_view(request):
    context = {}
    return render(request, "products/products_create.html", context)



# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "products/products_create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description,
    }
    return render(request, "products/products_detail.html", context)