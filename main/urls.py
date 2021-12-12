from django.urls import path

from .views import send, img

urlpatterns = [
    path('', send),
    path('message_id=<message_id>&user_id=<user_id>', img, name='send_mail')
]
