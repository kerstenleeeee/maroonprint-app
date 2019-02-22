# License
# Author: Hannah Mae Magno
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Magno - 02/17/19 - Added the forms for add functionality
# Lee - 02/18/19 - Edited floorNo choicefield and floorID plaeeholder
# Magno - 02/19/19 - Final commit

# File creation date: 02/17/19
# Development Group: 3
# Client Group: 3
# Description: Forms for the add blueprint functionality

from django import forms
from .models import Building, Floor

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = [
            'buildID', 
            'buildName',
            'buildFloors'
        ]

class BuildingCreateForm(forms.Form):
    buildID = forms.CharField(widget=forms.TextInput
        (attrs={'placeholder':'ex. dcs001'}))
    buildName = forms.CharField()
    buildFloors = forms.IntegerField()

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = [
            'buildID',  
	        #'floorID',  
            'floorNo',   
            'floorImageLink'  
        ]

class FloorCreateForm(forms.Form):
    buildID = forms.ModelChoiceField(queryset=Building.objects.all())
    #if buildID == "dcs001":
      #  print("ok")
    #floorID = forms.CharField(widget=forms.TextInput
     #   (attrs={'placeholder':'ex. dcs00'}))
    #floorID = forms.ModelChoiceField
    #floorNo = forms.IntegerField()
    floorNo = forms.IntegerField()
    #floorID = forms.CharField(default="%s %d" % (buildID, Floor.objects.get(floorNo)))
    floorImageLink = forms.URLField()