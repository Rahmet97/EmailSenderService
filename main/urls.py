from django.urls import path

from .views import send, ok

urlpatterns = [
    path('', send),
]
