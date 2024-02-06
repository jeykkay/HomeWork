from django.shortcuts import render, redirect
from django.views.generic import View

# from forum.forms import CommentForm
from forum.models import Topic, Comment
# from forum.forms import CommentForm


class HomePageView(View):
    def get(self, request):
        topics = Topic.objects.all()
        return render(request, 'homepage.html', {'Title': 'Home Page', 'topics': topics})


class AutoCommentView(View):
    def get(self, request):
        comments = Comment.objects.all()
        return render(request, 'auto_page.html', {'Title': 'comments_auto', 'comments': comments})


class SportCommentView(View):
    def get(self, request):
        comments = Comment.objects.all()
        return render(request, 'sport_page.html', {'Title': 'comments_sport', 'comments': comments})
