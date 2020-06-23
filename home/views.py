from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def entry(request):
    return render(request, 'home/entryPage.html')


def home(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['messageContent']
        send_mail(
            'Custom Piece Request',
            'You have a new request for a custom piece! \n\nName: ' + firstName + ' ' + lastName + '\nEmail: ' + email
            + '\nPhone Number: ' + phone + '\n\nMessage: ' + message,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return render(request, 'home/confirm.html', {'title': 'Confirm'})

    return render(request, 'home/mainPage.html', {'title': 'Homepage'})

# Create your views here.
