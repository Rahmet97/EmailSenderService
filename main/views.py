from django.contrib.auth.models import User
from django.shortcuts import render
from .tasks import send_email


def send(request):
    send_email.apply_async()
    return render(request, 'index.html')
