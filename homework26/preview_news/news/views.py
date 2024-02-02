from django.shortcuts import render

from django.views.generic import View

from news.models import News


class HomePage(View):
    def get(self, request):
        news = News.objects.order_by('date')
        return render(request, 'homepage.html', {'news': news, 'Title': 'Home Page'})
