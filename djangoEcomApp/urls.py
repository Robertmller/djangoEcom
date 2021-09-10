from .views import index, Shop, Contact, Blog, About, Account
from django.urls import path, include
from djangoEcomApp import views


urlpatterns = [
    path('', index, name='Home'),
    path('shop', Shop, name='Loja'),
    path('contact', Contact, name='Contato'),
    path('blog', Blog, name='Blog'),
    path('about', About, name='Sobre'),
    path('account', Account, name='Conta'),
]
