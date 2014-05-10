from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=99, blank=True, null=True)
    content = model.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return '{} - {} - {}'.format(self.title, self.author, self.created)
