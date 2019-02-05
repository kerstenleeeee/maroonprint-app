from django.urls import path
from django.conf.urls import url
from . import views
from .views import homePageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('', homePageView, name='home')
    #path('', homePageView.as_view(), name='home'),
    url(r'^$', views.homePageView, name="home"),
    url('about/', views.aboutPageView, name="about"),
    #dcs
    url('department-of-computer-science/', views.dcsPageView, name="dcs"),
    #engglib2
    url('engineering-library-ii/', views.enggLib2PageView, name="engglib21"),
    #coe
    url('college-of-engineering/', views.coePageView, name="coe"),
    #url(r'^new/$', views.new),
    #eee
    url('electrical-and-electronics-engineering-institute/', views.eeePageView, name="eee"),
    #ice
    url('institute-of-civil-engineering/', views.icePageView, name="ice"),
    #mmm
    url('mining-metallurgical-materials/', views.mmmPageView, name="mmm"),
    #che
    url('department-of-chemical-engineering/', views.chePageView, name="che"),
]

urlpatterns += staticfiles_urlpatterns()