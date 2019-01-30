from rest_framework import serializers
from .models import Building, Floor

class BuildingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Building
		fields = ('buildID', 'buildName',)

class FloorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Floor
		fields = ('buildID', 'floorID', 'floorNo',)