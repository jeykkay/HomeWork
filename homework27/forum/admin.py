from django.contrib import admin

from .models import Topic, Comment


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content',)
    search_fields = ('name', )
