from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.

from django.shortcuts import render, get_object_or_404
from . models import Product,Category,AltCategory,MarkaModel
from django.views import View

class CategoryView(View):
    def get(self,request,slug):
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category__slug=slug)
        categories = Category.objects.all()
        cok_satans = Product.objects.filter(cok_satan=True)[0:10]
        markas = MarkaModel.objects.all()

        return render(request, 'products/category.html', locals())


class AltCategoryView(View):
    def get(self,request,slug):
        category = get_object_or_404(AltCategory, slug=slug)
        products = Product.objects.filter(altcategory__slug=slug)
        categories = Category.objects.all()
        cok_satans = Product.objects.filter(cok_satan=True).order_by('-create_date')[0:10]
        markas = MarkaModel.objects.all()

        return render(request, 'products/category.html', locals())
    


class MarkaCategoryView(View):
    def get(self,request,slug):
        category = get_object_or_404(MarkaModel, slug=slug)
        products = Product.objects.filter(marka__slug=slug)
        categories = Category.objects.all()
        cok_satans = Product.objects.filter(cok_satan=True).order_by('-create_date')[0:10]
        markas = MarkaModel.objects.all()

        return render(request, 'products/category.html', locals())
    


def ProductDetailView(request, category_slug, slug):
    product = get_object_or_404 (Product, category__slug=category_slug, slug=slug)
    populers = Product.objects.filter(cok_satan=True).order_by('-create_date')[0:10]

    context = {
        'product' : product,
        'populers' : populers
    }
    return render(request, 'products/product_detail.html', context)


class ProductView(View):
    def get(self,request):
        products = Product.objects.filter(is_active=True)
        categories = Category.objects.all()
        cok_satans = Product.objects.filter(cok_satan=True)
        markas = MarkaModel.objects.all()
    

        return render(request, 'products/products.html', locals())
    

def SearchView(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(title__contains=searched)

        context = {
            'searched' : searched,
            'products' : products,
        }
        messages.success(request, ('Aradığınız Kelime İle İlgili Ürünler Aşağıda Sıralanmıştır'))
        return render(request, 'products/search.html', context)
    else:
        return render(request, 'products/search.html')

        

    


