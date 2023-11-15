from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Product, Category, AltCategory, MarkaModel


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.all()
    
    

class CategorySitemap(Sitemap):

    def items(self):
        return Category.objects.all()

    
class AltCategorySitemap(Sitemap):

    def items(self):
        return AltCategory.objects.all()


class MarkaSitemap(Sitemap):

    def items(self):
        return MarkaModel.objects.all()
