import datetime

from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Message
from .tasks import send_email


def send(request):
    users = User.objects.all()
    msg = Message.objects.filter(date=datetime.datetime.now()).first()
    send_email.apply_async(args=(users, msg))
    return render(request, 'index.html')