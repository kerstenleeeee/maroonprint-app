from rest_framework import serializers
from .models import Passenger, Bus, Terminal, Driver, Trip, Rating, Booking, Bus_Trip, Bus_Driver, CurrentTerminal

class PassengerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Passenger
		fields = ('userID', 'displayName',)

class BusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus
		fields = ('busID',)

class TerminalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Terminal
		fields = ('terminalID', 'terminalName',)

class DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Driver
		fields = ('driverID', 'displayName',)

class TripSerializer(serializers.ModelSerializer):
	class Meta:
		model = Trip
		fields = ('tripID', 'departureDate', 'departureTime', 'sourceTerminal', 'destinationTerminal', 'seatsLeft','price')

class RatingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rating
		fields = ('userID', 'tripID', 'rating',)

class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ('userID', 'tripID',)

class Bus_TripSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus_Trip
		fields = ('busID', 'tripID',)

class Bus_DriverSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bus_Driver
		fields = ('busID', 'driverID',)

class CurrentTerminalSerializer(serializers.ModelSerializer):
	class Meta:
		model = CurrentTerminal
		fields = ('terminalID', 'tripID',)



'''
from tickets.serializers import PassengerSerializer, BusSerializer, TerminalSerializer,DriverSerializer,TripSerializer,RatingSerializer,BookingSerializer,Bus_TripSerializer,Bus_DriverSerializer,CurrentTerminalSerializer
serializer = PassengerSerializer()
print(repr(serializer))
serializer = BusSerializer()
print(repr(serializer))
serializer = TerminalSerializer()
print(repr(serializer))
serializer = DriverSerializer()
print(repr(serializer))
serializer = TripSerializer()
print(repr(serializer))
serializer = RatingSerializer()
print(repr(serializer))
serializer = BookingSerializer()
print(repr(serializer))
serializer = Bus_TripSerializer()
print(repr(serializer))
serializer = Bus_DriverSerializer()
print(repr(serializer))
serializer = CurrentTerminalSerializer()
print(repr(serializer))


'''