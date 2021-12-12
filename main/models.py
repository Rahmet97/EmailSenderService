from django.db import models


class Message(models.Model):
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics', default=None, null=True)

    def __str__(self):
        return self.subject


class SentMessage(models.Model):
    choices = (
        (0, 'Not opened'),
        (1, 'Opened')
    )
    subject = models.CharField(max_length=50)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, default=None, null=True)
    text = models.TextField()
    status = models.CharField(choices=choices, max_length=10, default=None)
    to = models.EmailField()
    sent_time = models.DateTimeField(auto_now=True)
