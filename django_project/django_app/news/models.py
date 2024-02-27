from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class News(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False, unique=False)
    content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
