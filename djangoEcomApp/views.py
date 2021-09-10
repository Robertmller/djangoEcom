from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Shop(request):
    return render(request, 'shop.html')

def Contact(request):
    return render(request, 'contact.html')

def Blog(request):
    return render(request, 'blog.html')

def About(request):
    return render(request, 'about.html')

def Account(request):
    return render(request, 'account.html')