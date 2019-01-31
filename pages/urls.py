from django.urls import path
from django.conf.urls import url
from . import views
from .views import homePageView

urlpatterns = [
    #path('', homePageView, name='home')
    #path('', homePageView.as_view(), name='home'),
    url(r'^$', views.homePageView),
]