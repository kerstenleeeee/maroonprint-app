# License
# Author: Kristine-Clair Lee
# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
# of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019 

# Code History
# Lee - 01/30/19 - Initial Commit
# Lee - 01/30/19 - Added homePageView and aboutPageView
# Lee - 01/31/19 - Added dcsPageView
# Lee - 02/04/19 - Added more views
# Lee - 02/18/19 - Fixed views functionality

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

from django.db import IntegrityError

# viwew home.html
def homePageView(request):
	#return HttpResponse('MaroonPrint')
	return render(request, 'home.html')

# view about.html
def aboutPageView(request):
	# return HttpResponse('MaroonPrint')
	# weather = Floor.objects.get(buildID='ice001', floorID='ice02')
	# return render(request, 'about.html', {'weather':weather.floorImageLink})
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
			# Floor.objects.create(**form.cleaned_data)
			checkBuild = form.cleaned_data.get("buildID")
			checkFloor = form.cleaned_data.get("floorID")
			try:
				#varBuild = Floor.objects.get(buildID=checkBuild, floorID=checkFloor)
				#context = {
				#"form" : form,
				#"error" : "Blueprint already exists."
				#}
				#return render(request, 'add.html', context)
				Floor.objects.create(**form.cleaned_data)	
				messages.success(request, 'Successfully added the blueprint!')
				return HttpResponseRedirect('/add/')
			except IntegrityError as e:
				messages.error(request, 'Blueprint already exists. If you want to edit the blueprint, please go to the EDIT panel.')
		else:
			print(form.errors)
	context = {
		"form" : form
	}
	return render(request, 'add.html', context)

# view dcs.html
def dcsPageView(request):
	if Floor.objects.filter(buildID='dcs001', floorID='dcsLobby').exists():
		try:
			getFloors = Floor.objects.filter(buildID='dcs001')	# get all info inluding the floorImageLink
			dcsFloors = []
			for floors in getFloors:
				dcsFloors.append(floors.floorID)	# list of the floorIDs for hecking
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'dcs.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view engglib2.html
def enggLib2PageView(request):
	if Floor.objects.filter(buildID='engglib2001', floorID='engglib2Lobby').exists():
		try:
			getFloors = Floor.objects.filter(buildID='engglib2001')	# get all info inluding the floorImageLink
			engglib2Floors = []
			for floors in getFloors:
				engglib2Floors.append(floors.floorID)	# list of the floorIDs for hecking
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'engglib2.html', {"engglib2Floors" : engglib2Floors, "getFloors" : getFloors})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view coe.html
def coePageView(request):
	if Floor.objects.filter(buildID='coe001', floorID='coeLobby').exists():
		try:
			getFloors = Floor.objects.filter(buildID='coe001')	# get all info inluding the floorImageLink
			coeFloors = []
			for floors in getFloors:
				coeFloors.append(floors.floorID)	# list of the floorIDs for hecking
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'coe.html', {"coeFloors" : coeFloors, "getFloors" : getFloors})
		except:
			return render(request, 'error.html')
	else:
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