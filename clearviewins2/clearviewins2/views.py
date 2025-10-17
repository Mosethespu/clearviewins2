from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')

def contact(request):
    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def blog(request):
    return render(request, 'blog.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
