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
# Description: Urls for the pages

from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from . import views
from .views import homePageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('', homePageView, name='home')
    #path('', homePageView.as_view(), name='home'),
    url(r'^$', views.homePageView, name="home"),
    url('about/', views.aboutPageView, name="about"),
    url('error/', views.errorFloor, name="error"),
    url('error0/', views.errorAdmin, name="error-admin"),
    url('accounts/', include('django.contrib.auth.urls')),
    # url('login-landing/', views.loginLanding, name="loginLanding"),
    url('search-view/', views.searchPageView, name="search-view"),
    url('admin-page/',views.adminPageView, name="admin-page"),
    url('add-page/',views.addBuildingFloorRoutePageView, name="add-page"),
    url('add-building/',views.addBuildingPageView, name="add-building"),
    url('add-route/',views.addRoutePageView, name="add-route"),
    url('add-floor/',views.addFloorPageView, name="add-floor"),
    ###########
    url('delete-page/',views.deletePageView, name="delete-page"),
    url('delete-floor/',views.deleteFloorPageView, name="delete-floor"),
    url('delete-route/',views.deleteRoutePageView, name="delete-route"),
    url('delete-building/',views.deleteBuildingPageView, name="delete-building"),
    ##########
    url('edit-page/',views.editPageView, name="edit-page"),
    url('edit-building/',views.editBuildingPageView, name="edit-building"),
    url('edit-floor/',views.editFloorPageView, name="edit-floor"),
    url('edit-route/',views.editRoutePageView, name="edit-route"),
    ##########
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
    #dieor
    url('department-of-industrial-engineering/', views.iePageView, name="dieor"),
    #dge
    url('department-of-geodetic-engineering/', views.gePageView, name="dge"),
    #dme
    url('department-of-mechanical-engineering/', views.mePageView, name="dme"),
    #nec
    url('national-engineering-center/', views.necPageView, name="nec"),
]

urlpatterns += staticfiles_urlpatterns()