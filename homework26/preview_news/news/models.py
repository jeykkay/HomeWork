from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='image/', blank=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    comments = models.TextField()

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    nick_name = models.CharField(max_length=128, null=False, blank=False)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    news = models.ForeignKey('News', on_delete=models.CASCADE, related_name='comments_news')

    def __str__(self):
        return f'{self.nick_name}'
