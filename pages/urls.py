from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('hakkimizda/', views.About, name='about'),
    path('iletisim/', views.Contact, name='contact'),
]
