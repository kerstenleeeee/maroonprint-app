# License
# Author: Hannah Mae Magno
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 02/17/19 - Added the forms for add functionality
# Lee - 02/18/19 - Final commit

# File creation date: 02/17/19
# Development Group: 3
# Client Group: 3
# Description: Forms for the add blueprint functionality

from django import forms
from .models import Building, Floor

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = [
            'buildID',  
	        'floorID',  
            'floorNo',   
            'floorImageLink'  
        ]

class FloorCreateForm(forms.Form):
    buildID = forms.ModelChoiceField(queryset=Building.objects.all())
    floorID = forms.CharField(widget=forms.TextInput
        (attrs={'placeholder':'ex. dcs00'}))
    #floorID = forms.ModelChoiceField
    #floorNo = forms.IntegerField()
    floorNo = forms.ChoiceField(choices=[(x,x) for x in range(0,6)])
    floorImageLink = forms.URLField()