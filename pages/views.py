# License
# Author: Kristine-Clair Lee
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 01/30/19 - Initial Commit
# Lee - 01/30/19 - Added homePageView and aboutPageView
# Lee - 01/31/19 - Added dcsPageView
# Lee - 02/04/19 - Added more views

# File creation date: 01/30/19
# Development Group: 3
# Client Group: 3
# Description: Home landing page. Serves as the primary landing page of the maroonprint application.

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
		return render(request, 'dcs.html')
	except:
		return render(request, 'error.html')

def enggLib2PageView(request):
	try:
		entriesB = Building.objects.get(buildID='engglib2001')
		return render(request, 'engglib2.html')
	except:
		return render(request, 'error.html')

def coePageView(request):
	try:
		entriesB = Building.objects.get(buildID='coe001')
		return render(request, 'coe.html')
	except:
		return render(request, 'error.html')

def eeePageView(request):
	try:
		entriesB = Building.objects.get(buildID='eee001')
		return render(request, 'eee.html')
	except:
		return render(request, 'error.html')

def icePageView(request):
	try:
		entriesB = Building.objects.get(buildID='ice001')
		return render(request, 'ice.html')
	except:
		return render(request, 'error.html')

def mmmPageView(request):
	try:
		entriesB = Building.objects.get(buildID='mmm001')
		return render(request, 'mmm.html')
	except:
		return render(request, 'error.html')

def chePageView(request):
	try:
		entriesB = Building.objects.get(buildID='che001')
		return render(request, 'che.html')
	except:
		return render(request, 'error.html')