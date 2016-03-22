from __future__ import unicode_literals

from django.db import models

class Idea(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name