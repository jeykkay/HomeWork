from django.contrib import admin

from News.models import News, Comment

admin.site.register(News)
admin.site.register(Comment)
