from .forms import RawProductForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
from django.http import Http404


# def product_create_view(request):
#     my_form = RawProductForm()

#     if request.method == 'POST':
#         my_form = RawProductForm(request.POST)  # request.POST will show the field validation required as a msg or warning if we hover the pointer in the field

#         if my_form.is_valid():
#             print(my_form.cleaned_data) # the data after successful validation
#             Product.objects.create(**my_form.cleaned_data)
            
#         else:
#             print(my_form.errors)   # if it's an invalid in input, eg: if we enter a letter where only numbers are allowed
            
        
#     context = {
#         'form': my_form
#     }
#     return render(request, 'products/product_create.html', context)


# def product_create_view(request):
#     if request.method == 'POST':
#         my_title = request.POST.get('title')
#         print(my_title)
        
#     context = {}
#     return render(request, "products/product_create.html", context)


def product_create_view(request):
    initial_data = {
        'title': 'My title'
    }
    obj = Product.objects.get(id=1)
    
    form = ProductForm(request.POST or None, initial=initial_data, instance=obj)   # request.POST or None renders if post data is true or else renders out empty form
    
    if form.is_valid():
        form.save()
        form = ProductForm()
        
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=my_id)
    # obj = get_object_or_404(Product, id=my_id)
    
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     "title": obj.title,
    #     "description": obj.description,
    # }
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('../')
        
    context = {
        'object': obj
    }
    return render(request, 'products/product_delete.html', context)
