# License
# Author: Kristine-Clair Lee
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 01/30/19 - Initial Commit
# Lee - 01/30/19 - Added serializers

# File creation date: 01/30/19
# Development Group: 3
# Client Group: 3
# Description: Serializers for the models for the database

from rest_framework import serializers
from .models import Building, Floor

# building serializer
class BuildingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Building
		fields = ('buildID', 'buildName',)

# floor serializer
class FloorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Floor
		fields = ('buildID', 'floorID', 'floorNo',)