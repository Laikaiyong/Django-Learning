from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, RawProductForm
from .models import Product

# def product_create_view(request):
#     initial_data = {
        #   'title': 'New Product'
#     }
#     form = RawProductForm(initial=initial_data)
##     form = RawProductForm(instance = Product.objects.get(id=2))
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             Product.objects.create(
#                 **form.cleaned_data
#             )

def product_update_view(request, product_id):
    form = ProductForm(request.POST or None, instance = Product.objects.get(id=product_id))
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)
    
#     context = {
#         'title': 'Create New Product',
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'title': 'product',
#         'products': obj
#     }
#     return render(request, "product/product_detail.html", context)

def product_profile_view(request, product_id, *args, **kwargs):
    object = get_object_or_404(Product, id=product_id)
    # try:
    #     object = Product.objects.get(id=product_id)
    # except Product.DoesNotExist:
    #     raise Http404

    context = {
        "object": object
    }
    return render(request, "product/product_detail.html", context)

def product_delete_view(request, product_id):
    object = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        object.delete()
        return redirect('../../')
    
    context = {
        "object": object
    }
    return render(request, "product/product_delete.html", context)

def product_list_view(request, *args, **kwargs):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'product/product_list.html', context)