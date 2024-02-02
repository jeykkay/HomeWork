from django.contrib import admin

from news.models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'content', 'date', ]
    list_filter = ['date', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['nick_name', 'content', 'date', ]
