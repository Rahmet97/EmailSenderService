import datetime
from time import sleep

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import SentMessage, Message
from celery import shared_task


@shared_task
def send_email():
    sleep(10)
    try:
        users = User.objects.filter(is_superuser=0)
        msg = Message.objects.filter(Q(date__lt=datetime.datetime.now()-datetime.timedelta(seconds=30)), Q(is_sent=False))
        for j in msg:
            for i in users:
                html_message = render_to_string('email.html', {'subject': j.subject, 'message': j.message, 'user': i})
                thoughts = strip_tags(html_message)

                sender = settings.EMAIL_HOST_USER
                recipients = [i.email]
                email_msg = EmailMultiAlternatives(
                    j.subject,
                    thoughts,
                    sender,
                    recipients
                )
                email_msg.attach_alternative(html_message, 'text/html')
                email_msg.send()
                j.is_sent = True
                j.save()
                # message = 'Dear ' + i.first_name + ' ' + i.last_name + '. ' + j.message
                # cr_msg = SentMessage.objects.create(subject=j.subject, text=message, status=0, to=i.email)
                # cr_msg.save()
    except Exception as e:
        raise e
