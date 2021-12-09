from django.urls import path

from main.views import send

urlpatterns = [
    path('', send),
]
