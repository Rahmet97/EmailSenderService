from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http.response import JsonResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import SentMessage
from EmailSender.celery import app


@app.task
def send_email(users, msg):
    for i in users:
        message = 'Dear' + i.first_name + ' ' + i.last_name + '\n' + msg.message
        html_message = render_to_string('email.html', {'subject': msg.subject, 'message': message})
        thoughts = strip_tags(html_message)

        sender = settings.EMAIL_HOST_USER
        recipients = [i.email]
        email_msg = EmailMultiAlternatives(
            msg.subject,
            thoughts,
            sender,
            recipients
        )
        email_msg.attach_alternative(html_message, 'text/html')
        email_msg.send()

        cr_msg = SentMessage.objects.create(subject=msg.subject, text=message, status=0, to=i.email)
        cr_msg.save()
    return JsonResponse({'success': True})