from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.CategoryView.as_view(), name='category'),
    path('kategori/<slug:slug>/', views.AltCategoryView.as_view(), name='altcategory'),
    path('<slug:category_slug>/<slug:slug>/', views.ProductDetailView, name='product_detail'),
    path('kategori/marka/<slug:slug>/', views.MarkaCategoryView.as_view(), name='marka'),
    path('hirdavat/bahce-yapi/tum-urunler/', views.ProductView.as_view(), name= 'products'),
    path('search/arama/ara/', views.SearchView, name='search'),
]
