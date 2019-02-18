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
    floorID = forms.CharField()
    floorNo = forms.IntegerField()
    floorImageLink = forms.URLField()