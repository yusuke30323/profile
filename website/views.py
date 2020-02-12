from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def news(request):
    return render(request, 'news.html', {})

def profile(request):
    return render(request, 'profile.html', {})
