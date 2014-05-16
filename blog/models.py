from django.db import models
from django.conf import settings
from django.utils import timezone

from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=99, blank=True, null=True)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User)

    def __unicode__(self):
        return '{}, {} | {}'.format(self.title, self.author, self.created)



