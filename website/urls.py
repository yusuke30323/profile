from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact.html', views.contact, name = 'contact'),
    path('news.html', views.news, name = 'news'),
    path('profile.html', views.profile, name = 'profile'),
]
