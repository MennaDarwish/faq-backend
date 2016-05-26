from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Profile(models.Model):
    """
    A User's profile
    """
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='profile/', null=True)
    bio = RichTextField(blank=True)
    company_field = models.CharField(max_length=256)

    def __unicode__(self):
        return self.user.username


class Question(models.Model):
    """
    A single Question entry
    """
    body = models.TextField()
    title = models.CharField(max_length=256)
    attachment = models.FileField(upload_to='uploads/')

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    """
    A single Tag entry
    """
    question = models.ForeignKey(Question, related_name='tags')
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return '%s' % (self.name)


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers')
    answer_body = models.TextField()
    accepted = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s: %s' % (self.question, self.answer_body)
