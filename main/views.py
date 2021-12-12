from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import os
from .models import Message, SentMessage
from .tasks import send_email


def send(request):
    send_email.delay()
    return render(request, 'index.html')


def img(request, message_id, user_id):
    msg = Message.objects.get(id=message_id)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_dir = script_dir.replace('/main', '')
    print(os.path.join(script_dir + msg.image.url))
    image_data = open(os.path.join(script_dir + msg.image.url), 'rb').read()
    email = User.objects.get(id=user_id).email
    try:
        sent_msg = SentMessage.objects.get(Q(message_id=message_id) and Q(to=email) and Q(status=0))
    except:
        sent_msg = None
    if sent_msg is not None:
        sent_msg.status = 1
        sent_msg.save()
    return HttpResponse(image_data, content_type="image/png")
