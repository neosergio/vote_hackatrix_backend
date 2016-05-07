from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Idea(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    votes = models.IntegerField(default=0)
    register = models.ForeignKey(User, null=True, blank=True, editable=False)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Outstanding(models.Model):
    name = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    comment = models.TextField()
    idea = models.ForeignKey(Idea)
    register = models.ForeignKey(User, null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name
