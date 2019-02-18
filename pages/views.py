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
# Description: Views for the pages

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

from bps.forms import FloorForm, FloorCreateForm
from django.contrib import messages	

# viwew home.html
def homePageView(request):
	#return HttpResponse('MaroonPrint')
	return render(request, 'home.html')

# view about.html
def aboutPageView(request):
	#return HttpResponse('MaroonPrint')
	return render(request, 'about.html')

def errorFloor(request):
	return render(request, 'error.html')

def loginLanding(request):
	return render(request, 'login-landing.html')

def adminPageView(request):
	return render(request, 'admin-page.html')

def addPageView(request):
	return render(request, 'add.html')

def addPageView(request):
	form = FloorCreateForm()
	if request.method == "POST":
		form = FloorCreateForm(request.POST)	
		if form.is_valid():
			#form.save()
			print(form.cleaned_data)
			Floor.objects.create(**form.cleaned_data)
			messages.success(request, 'Successfully added the blueprint!')
			return HttpResponseRedirect('/add/')
		else:
			print(form.errors)
	context = {
		"form" : form
	}
	return render(request, 'add.html', context)

# view dcs.html
def dcsPageView(request):
	try:
		#dcsFloor1 = Floor.objects.filter(buildID = 'dcs001', floorNo = 1).values('floorImageLink')
		#dcsFloor2 = Floor.objects.filter(buildID = 'dcs001', floorNo = 2).values('floorImageLink')
		#dcsFloor3 = Floor.objects.filter(buildID = 'dcs001', floorNo = 3).values('floorImageLink')
		dcsFloor1 = Floor.objects.get(buildID='dcs001', floorNo = 1)
		#my_instance = dcsView.floorImageLink
		entriesB = Building.objects.get(buildID='dcs001')
		return render(request, 'dcs.html')
	except:
		return render(request, 'error.html')

# view engglib2.html
def enggLib2PageView(request):
	try:
		entriesB = Building.objects.get(buildID='engglib2001')
		return render(request, 'engglib2.html')
	except:
		return render(request, 'error.html')

# view coe.html
def coePageView(request):
	try:
		entriesB = Building.objects.get(buildID='coe001')
		return render(request, 'coe.html')
	except:
		return render(request, 'error.html')

# view  eee.html
def eeePageView(request):
	try:
		entriesB = Building.objects.get(buildID='eee001')
		return render(request, 'eee.html')
	except:
		return render(request, 'error.html')

# view ice.html
def icePageView(request):
	try:
		entriesB = Building.objects.get(buildID='ice001')
		return render(request, 'ice.html')
	except:
		return render(request, 'error.html')

# view mmm.html
def mmmPageView(request):
	try:
		entriesB = Building.objects.get(buildID='mmm001')
		return render(request, 'mmm.html')
	except:
		return render(request, 'error.html')

# view che.html
def chePageView(request):
	try:
		entriesB = Building.objects.get(buildID='che001')
		return render(request, 'che.html')
	except:
		return render(request, 'error.html')