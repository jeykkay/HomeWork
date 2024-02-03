from django.shortcuts import render

from django.views.generic import View

from news.models import News


class HomePage(View):
    def get(self, request):
        news = News.objects.all().values()
        return render(request, 'homepage.html', {'news': news, 'Title': 'Home Page'})


class SortingNews(View):
    def get(self, request):
        sorting_param = request.GET.get('name_sorting')
        priority_sorting = request.GET.get('priority_sorting')
        news = News.objects.order_by(f'{priority_sorting }{sorting_param}')
        return render(request, 'homepage.html', {'news': news, 'Title': 'Home Page'})
