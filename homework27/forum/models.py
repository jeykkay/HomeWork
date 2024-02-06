from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=128)


class Comment(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, unique=False)
    content = models.TextField()
