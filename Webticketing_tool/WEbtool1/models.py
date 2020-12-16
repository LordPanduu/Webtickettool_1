from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Ticket(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=50)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Ticket_detail', kwargs={'pk': self.pk})