from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Ekleyin", unique=True)
    is_home = models.BooleanField(verbose_name='Ana Sayfada Gösterilsin Mi? (3 Adet Kategori Seçebilirsimiz)')
    img = models.ImageField(upload_to='product/category/', blank=True, null=True)
    seotitle = models.CharField(max_length=60, verbose_name='Kategori Seo Title Gir', null=True)
    seodescription = models.CharField(max_length=160, verbose_name='Kategori Seo Description Gir', null=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/urunler/{self.slug}/'
    

class AltCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Ekleyin", unique=True)
    seotitle = models.CharField(max_length=60, verbose_name='AltKategori Seo Title Gir', null=True)
    seodescription = models.CharField(max_length=160, verbose_name='AltKategori Seo Description Gir', null=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/urunler/kategori/{self.slug}/'
    

class MarkaModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Marka Oluşturunuz', unique=True)
    seotitle = models.CharField(max_length=60, verbose_name='Marka Seo Title Gir', null=True)
    seodescription = models.CharField(max_length=160, verbose_name='Marka Seo Description Gir', null=True)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'urunler/kategori/marka/{self.slug}/'
    
class Customer(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='İsim :', default='')
    last_name = models.CharField(max_length=20, verbose_name='Soyisim :', default='')
    phone = models.CharField(max_length=50, verbose_name='Telefon :', default='')
    email = models.EmailField(verbose_name='E mail ', default='')
    password = models.CharField(max_length=100, verbose_name='Parola :', default='')
    

class Product(models.Model):
    user = models.ForeignKey(User, verbose_name='Ürün Ekleyen', on_delete=models.CASCADE)
    stokno = models.CharField(max_length=30, verbose_name='Ürün Stok Numarası', null=True, blank=True, unique=True)
    title = models.CharField(max_length=200, verbose_name='Ürün Başlığı Giriniz', unique=True)
    seotitle = models.CharField(max_length=60, verbose_name='Seo Başlığı Giriniz', null=True)
    description = models.TextField(verbose_name='Ürün Açıklama', null=True)
    seodescription = models.TextField(verbose_name='Seo Açıklama Giriniz', null=True, max_length=160)
    img = models.ImageField(verbose_name="ürün Ana Resmi", upload_to='product/%Y/%m/%d/')
    marka = models.ForeignKey(MarkaModel, on_delete=models.CASCADE, verbose_name='Ürün Markası Girin', null=True)
    price = models.DecimalField(verbose_name='Ürün Fiyatı', decimal_places=2, max_digits=6, default=0)
    is_sale = models.BooleanField(default=False, verbose_name="Ürün İndirimli Mi?")
    sale_price = models.DecimalField(verbose_name='Ürün İndirimli Fiyatı', decimal_places=2, max_digits=6, blank=True, default=0)
    indirimoran = models.IntegerField(null=True, verbose_name='İndirim Oranı Yüzde Kaç?', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Ürün Kategori Giriniz?')
    altcategory = models.ManyToManyField(AltCategory, verbose_name='Ürün Alt Kategori Giriniz?', blank=True)
    is_home = models.BooleanField(default=True, verbose_name='Ürün Ana Sayfada Gösterilsin Mi?')
    is_active = models.BooleanField(default=True, verbose_name='Ürün Mevcut Mu?')
    stok = models.IntegerField(verbose_name='Ürün Mevcut İse Stok Adedi Giriniz')
    is_yeni = models.BooleanField(verbose_name='Ürün Yeni Mi?')
    img1 = models.ImageField(verbose_name="ürün Detay 1. Resmi", upload_to='product/%Y/%m/%d/', blank=True)
    img2 = models.ImageField(verbose_name="ürün Detay 2. Resmi", upload_to='product/%Y/%m/%d/', blank=True)
    img3 = models.ImageField(verbose_name="ürün Detay 3. Resmi", upload_to='product/%Y/%m/%d/', blank=True)
    urun_ayrinti = RichTextUploadingField(verbose_name='Ürün Ayrıtılı Bilgi')
    boy = models.IntegerField(verbose_name="Ürün Boyu Cm", blank=True)
    agirlik = models.IntegerField(verbose_name="Ürün Ağırlık Kg", blank=True) 
    uzunluk = models.IntegerField(verbose_name="Ürün Boyu Cm", blank=True)
    genislik = models.IntegerField(verbose_name="Ürün Genişlik Cm", blank=True)
    derinlik = models.IntegerField(verbose_name="Ürün Derinlik Cm", blank=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Ürün Eklenme Tarihi')
    upgrade_date = models.DateTimeField(auto_now=True, verbose_name='Ürün Güncellenme Tarihi')
    cok_satan = models.BooleanField(verbose_name='Çok Satanlarda Mı?')
    slug = models.SlugField(unique=True, blank=True)

    
    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title
    
    def get_display_price(self):
        return self.price / 10
    
    def get_absolute_url(self):
        return f'/urunler/{self.category.slug}/{self.slug}/'
 

class CarouselModel(models.Model):
    img = models.ImageField(verbose_name="Slider Resmi Ekle", upload_to='carousel/%Y/%m/%d/')
    name = models.CharField(max_length=200, verbose_name='Caroseul Açıklama Gir', null=True)
    description = models.TextField(verbose_name='Açıklama Girin', null=True)

    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    adress = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=11, default='')
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    
    def __str__(self):
        return self.product
   