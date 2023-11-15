from django.contrib import admin
from . models import Category, Product, AltCategory, MarkaModel,CarouselModel,Order,Customer


@admin.register(Product)
class PruductAdmin(admin.ModelAdmin):
    list_display = ('title','img','id','price','sale_price','is_active','stok','category',)
    list_filter = ('is_active', )
    search_fields = ('title', 'description',)
    prepopulated_fields = {'slug':('title',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(AltCategory)
class AltCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(MarkaModel)
class MarkaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}

admin.site.register(CarouselModel)

admin.site.register(Customer)
admin.site.register(Order)

