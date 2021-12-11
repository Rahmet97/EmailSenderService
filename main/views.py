from django.shortcuts import render
from .tasks import send_email, email


def send(request):
    send_email.delay(10)
    return render(request, 'index.html')


def ok(request):
    email()
    return render(request, 'index.html')
