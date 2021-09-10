from .views import index, 
from django.urls import path, include
from djangoEcomApp import views


urlpatterns = [
    path('index.html', index, name='Home'),
    path('shop.html', shop, name='Loja'),
    path('contact.html', contact, name='Contato'),
    path('blog.html', blog, name='Blog'),
    path('about.html', about, name='Sobre'),
    path('account.html', account, name='Conta'),
]
