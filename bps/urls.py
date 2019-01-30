from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bps import views

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'),
    path('building/', views.BuildingList),
    path('floor/', views.FloorList),
]
urlpatterns = format_suffix_patterns(urlpatterns)