from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=128, blank=False, null=False, unique=True)


class Comment(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=False, null=False, unique=False)
    content = models.TextField()
