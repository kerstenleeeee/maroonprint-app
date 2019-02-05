from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bps.models import Building, Floor
from bps.serializers import BuildingSerializer, FloorSerializer
from rest_framework import status

# Create your views here.
def homePageView(request):
	#return HttpResponse('MaroonPrint')
	return render(request, 'home.html')

def aboutPageView(request):
	#return HttpResponse('MaroonPrint')
	return render(request, 'about.html')

def dcsPageView(request):
	try:
		entriesB = Building.objects.get(buildID='dcs001')
		entriesF = Floor.objects.get(buildID='dcs001', floorID='dcs02')
		return render(request, 'dcs.html')
	except:
		return render(request, 'error.html')

def enggLib2PageView(request):
	try:
		entriesB = Building.objects.get(buildID='engglib2001')
		entriesF = Floor.objects.get(buildID='engglib2001', floorID='engglib21')
		return render(request, 'dcs.html')
	except:
		return render(request, 'error.html')

def coePageView(request):
	try:
		entriesB = Building.objects.get(buildID='coe001')
		entriesF = Floor.objects.get(buildID='coe001', floorID='coe01')
		return render(request, 'coe.html')
	except:
		return render(request, 'error.html')

def eeePageView(request):
	try:
		entriesB = Building.objects.get(buildID='eee001')
		entriesF = Floor.objects.get(buildID='eee001', floorID='eee01')
		return render(request, 'eee.html')
	except:
		return render(request, 'error.html')

def icePageView(request):
	try:
		entriesB = Building.objects.get(buildID='ice001')
		entriesF = Floor.objects.get(buildID='ice001', floorID='ice01')
		return render(request, 'ice.html')
	except:
		return render(request, 'error.html')

def mmmPageView(request):
	try:
		entriesB = Building.objects.get(buildID='mmm001')
		entriesF = Floor.objects.get(buildID='mmm001', floorID='mmm01')
		return render(request, 'mmm.html')
	except:
		return render(request, 'error.html')

def chePageView(request):
	try:
		entriesB = Building.objects.get(buildID='che001')
		entriesF = Floor.objects.get(buildID='che001', floorID='che01')
		return render(request, 'che.html')
	except:
		return render(request, 'error.html')