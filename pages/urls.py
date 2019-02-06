# License
# Author: Kristine-Clair Lee
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 01/30/19 - Initial Commit
# Lee - 01/30/19 - Added url for dcs and coe
# Lee - 01/31/19 - Added url for engglib2
# Lee - 02/04/19 - Added more urls

# File creation date: 01/30/19
# Development Group: 3
# Client Group: 3
# Description: Home landing page. Serves as the primary landing page of the maroonprint application.

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
    url('engineering-library-ii/', views.enggLib2PageView, name="engglib2"),
    #coe
    url('college-of-engineering/', views.coePageView, name="coe"),
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