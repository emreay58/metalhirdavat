from django.urls import path
from . import views

urlpatterns = [
    path('kullanici/giris/', views.LoginView, name='login'),
    path('kullanici/cikis/', views.LogoutView, name='logout'),
    path('kullanici/kayit/', views.RegisterView, name='register'),
    path('kullanici/kayit/adres', views.AdresView, name='adres'),

]
