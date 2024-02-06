from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('autos/', views.AutoCommentView.as_view(), name='auto'),
    path('sports/', views.SportCommentView.as_view(), name='sport')
]