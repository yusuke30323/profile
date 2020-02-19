from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def news(request):
    return render(request, 'news.html', {})

def profile(request):
    return render(request, 'profile.html', {})


def contact(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_message = request.POST['your-message']
        your_email = request.POST['your-email']

        message = 'Name: ' + your_name + '\nEmail: ' + your_email + '\nMessage: ' + your_message

        send_mail(
            'Contact',
            message,
            your_email,
            ['ykonokono19970508@gmail.com'],
            )


        return render(request, 'contact.html', {'your_name':your_name})
    else:
        return render(request, 'contact.html', {})
