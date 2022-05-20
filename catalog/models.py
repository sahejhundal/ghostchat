from django.db import models

from django.urls import reverse # Used to generate URLs by reversing the URL patterns



class Message(models.Model):
    """Model representing a message"""
    username = models.CharField(max_length=20)
    userip = models.CharField(max_length=100)
    senttime = models.DateTimeField()
    content = models.TextField(max_length=1000, help_text='Type something')
    color=models.CharField(max_length=7, default="#000000")

    def __str__(self):
        """String for representing the Message object."""
        return f'{self.username}({self.senttime}): {self.content}'

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('message-detail', args=[str(self.id)])
