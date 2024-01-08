from django.db import models

from Article.models import Article

from Author.models import Author


class Comment(models.Model):
    text = models.CharField(max_length=255)
    articles = models.ManyToManyField(Article)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
