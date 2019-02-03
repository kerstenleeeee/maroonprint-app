from django.urls import path
from django.conf.urls import url
from . import views
from .views import homePageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('', homePageView, name='home')
    #path('', homePageView.as_view(), name='home'),
    url(r'^$', views.homePageView),
    #url(r'^dcs/$', views.dcsPageView),
    #url(r'^new/$', views.new),
]

urlpatterns += staticfiles_urlpatterns()