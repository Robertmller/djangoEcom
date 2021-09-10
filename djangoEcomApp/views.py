from django.shortcuts import render

def index(request):
    return render(request, 'html/index.html')

def Shop(request):
    return render(request, 'html/shop.html')

def Contact(request):
    return render(request, 'html/contact.html')

def Blog(request):
    return render(request, 'html/blog.html')

def About(request):
    return render(request, 'html/about.html')

def Account(request):
    return render(request, 'html/account.html')