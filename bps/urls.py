# License
# Author: Kristine-Clair Lee
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 01/30/19 - Initial Commit
# Lee - 01/30/19 - Added urls

# File creation date: 01/30/19
# Development Group: 3
# Client Group: 3
# Description: Home landing page. Serves as the primary landing page of the maroonprint application.

from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bps import views

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'),
    path('building/', views.BuildingList),
    path('floor/', views.FloorList),
    path('building/<str:pk>/', views.BuildingViews),
    path('floor/<str:pk>/', views.FloorViews)
]
urlpatterns = format_suffix_patterns(urlpatterns)