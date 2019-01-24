from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tickets import views

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'),
    path('passengers/', views.PassengerList),
    path('passengers/<str:pk>/', views.PassengerViews),
    path('buses/', views.BusList),
    path('buses/<str:pk>/', views.BusViews),
    path('terminals/', views.TerminalList),
    path('terminals/<str:pk>/', views.TerminalViews),
    path('driver/', views.DriverList),
    path('driver/<str:pk>/', views.DriverViews),
    path('trips/', views.TripList),
    path('trips/<str:pk>/', views.TripViews),
    path('rating/', views.RatingList),
    path('rating/<str:pk>/', views.RatingViews),
    path('rating/<str:user>/<str:trip>/', views.IndividualRatingViews),
    path('booking/', views.BookingList),
    path('booking/<str:user>/', views.BookingViews),
    path('booking/<str:user>/<str:trip>/', views.IndividualBookingViews),
    path('bus_trip/', views.Bus_TripList),
    #path('bus_trip/<#>', views.Bus_TripViews),
    path('bus_driver/', views.Bus_DriverList),
    #path('bus_driver/<#>', views.Bus_DriverViews),
    path('current_terminal/', views.CurrentTerminalList),
    #path('current_terminal/<#>', views.CurrentTerminalViews),
]
urlpatterns = format_suffix_patterns(urlpatterns)