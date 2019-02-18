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