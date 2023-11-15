from django.shortcuts import render
from products.models import Product,Category,CarouselModel


def Index(request):
    products = Product.objects.filter(is_home=True)[0:20]
    categories = Category.objects.filter(is_home=True)
    category = Category.objects.all()
    yeniler = Product.objects.filter(is_yeni=True)
    carousels = CarouselModel.objects.all()

    context={
        'products' : products,
        'categories' : categories,
        'category' : category,
        'yeniler' : yeniler,
        'carousels' : carousels
    } 

    return render(request, "pages/index.html", context)


def About(request):
    return render(request, "pages/about.html")

def Contact(request):
    return render(request, "pages/contact.html")


def error_404_view(request, exception):
    return render(request, 'pages/404.html')