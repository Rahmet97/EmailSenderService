from time import sleep

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import SentMessage, Message
from celery import shared_task


@shared_task
def send_email(duration):
    sleep(duration)
    try:
        users = User.objects.filter(is_superuser=0).first()
        msg = Message.objects.first()
        # for i in users:

        html_message = render_to_string('email.html', {'subject': msg.subject, 'message': msg.message, 'user': users})
        thoughts = strip_tags(html_message)

        sender = settings.EMAIL_HOST_USER
        recipients = ['rahmetruslanov6797@gmail.com']
        email_msg = EmailMultiAlternatives(
            msg.subject,
            thoughts,
            sender,
            recipients
        )
        email_msg.attach_alternative(html_message, 'text/html')
        email_msg.send()

        # message = 'Dear ' + i.first_name + ' ' + i.last_name + '. ' + msg.message
        # cr_msg = SentMessage.objects.create(subject=msg.subject, text=message, status=0, to=i.email)
        # cr_msg.save()
    except Exception as e:
        raise e


@shared_task
def email():
    send_mail('Test subject', 'Test message', settings.EMAIL_HOST_USER, ['rahmetruslanov6797@gmail.com'],
              fail_silently=True)
