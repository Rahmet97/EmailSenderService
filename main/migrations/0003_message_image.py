# Generated by Django 3.2.10 on 2021-12-12 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_message_is_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='pics'),
        ),
    ]
