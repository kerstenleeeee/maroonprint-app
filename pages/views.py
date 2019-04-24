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
from bps.models import Building, Floor, Routes
from bps.serializers import BuildingSerializer, FloorSerializer, RouteSerializer
from rest_framework import status

from bps.forms import FloorForm, FloorCreateForm, BuildingForm, BuildingCreateForm, DeleteFloor, RouteCreateForm, RouteForm, DeleteRoute, EditBuilding, DeleteBuilding
from django.contrib import messages	

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# viwew home.html
def homePageView(request):
	#return HttpResponse('MaroonPrint')
	getBuildings = Building.objects.all()
	#listBuildings = []
	#for buildings in getBuildings:
		#listBuildings.append(buildings.buildName)
	print(getBuildings)
	return render(request, 'home.html', {"getBuildings" : getBuildings})

# view about.html
def aboutPageView(request):
	# return HttpResponse('MaroonPrint')
	# weather = Floor.objects.get(buildID='ice001', floorID='ice02')
	# return render(request, 'about.html', {'weather':weather.floorImageLink})
	getBuildings = Building.objects.all()
	#listBuildings = []
	#for buildings in getBuildings:
		#listBuildings.append(buildings.buildName)
	print(getBuildings)
	return render(request, 'about.html', {"getBuildings" : getBuildings})

def searchPageView(request):
	# return HttpResponse('MaroonPrint')
	# weather = Floor.objects.get(buildID='ice001', floorID='ice02')
	# return render(request, 'about.html', {'weather':weather.floorImageLink})
	getBuildings = Building.objects.all()
	#listBuildings = []
	#for buildings in getBuildings:
		#listBuildings.append(buildings.buildName)
	print(getBuildings)
	return render(request, 'search.html', {"getBuildings" : getBuildings})

def errorFloor(request):
	return render(request, 'error.html')

def loginLanding(request):
	return render(request, 'login-landing.html')

def adminPageView(request):
	return render(request, 'admin-page.html')

def addBuildingFloorRoutePageView(request):
	return render(request, 'add-page.html')

def editPageView(request):
	return render(request, 'edit-page.html')

def deletePageView(request):
	return render(request, 'delete-page.html')

'''
def editFloorPageView(request):
	#return render(request, "edit-floor.html")
	form = FloorCreateForm()
	if request.method == "POST":
		form = FloorCreateForm(request.POST)
		if form.is_valid():
			checkBuild = form.cleaned_data.get("buildID")
			checkFloor = form.cleaned_data.get("floorNo")
			checkLink = form.cleaned_data.get("floorImageLink")
			if Floor.objects.filter(buildID=checkBuild, floorNo=checkFloor).exists():
				try:
					Floor.objects.filter(buildID=checkBuild, floorNo=checkFloor).update(floorImageLink=checkLink)
					messages.success(request, 'Successfully updated the blueprint!')
					return HttpResponseRedirect('/edit-floor/')
				except ObjectDoesNotExist:
					messages.error(request, 'Blueprint does not exist. If you want to add the blueprint, please go to the ADD panel.')
			else:
					messages.error(request, 'Blueprint does not exist. If you want to add the blueprint, please go to the ADD panel.')
		else:
			print(form.errors)	
	context = {
		"form" : form
	}
	return render(request, 'edit-floor.html', context)'''

def addBuildingPageView(request):
	form = BuildingCreateForm()
	if request.method == "POST":
		form = BuildingCreateForm(request.POST)	
		if form.is_valid():
			#form.save()
			print(form.cleaned_data)
			# Floor.objects.create(**form.cleaned_data)
			checkBuild = form.cleaned_data.get("buildID")
			checkFloor = form.cleaned_data.get("buildFloors")
			try:
				Building.objects.filter(buildName=checkBuild).update(buildExist=True, buildFloors=checkFloor)
				messages.success(request, 'Successfully added the building!')
				return HttpResponseRedirect('/add-building/')
			except IntegrityError as e:
				messages.error(request, 'Building already exists. If you want to add a blueprint (floor) to the building, please go to the "Add Floor" section.')
		else:
			print(form.errors)
	context = {
		"form" : form
	}
	return render(request, 'add-building.html', context)
	
def addFloorPageView(request):
	form = FloorCreateForm()
	if request.method == "POST":
		form = FloorCreateForm(request.POST)
		if form.is_valid():
			#form.save()
			#print(form.cleaned_data)
			# Floor.objects.create(**form.cleaned_data)
			checkBuild = form.cleaned_data.get("buildID")
			print(checkBuild.buildID)
			#if checkBuild.buildID == "dcs001":
			checkFloor = form.cleaned_data.get("floorNo")
			print(checkBuild)
			print(checkFloor)
			print(form.cleaned_data)
			if Floor.objects.filter(buildID=checkBuild, floorNo=checkFloor).exists():
				messages.error(request, 'Blueprint already exists. If you want to edit the blueprint, please go to the EDIT panel.')
			else:
				try:
					Floor.objects.create(**form.cleaned_data)	
					messages.success(request, 'Successfully added the blueprint!')
					return HttpResponseRedirect('/add-floor/')
				except IntegrityError as e:
					messages.error(request, 'Blueprint already exists. If you want to edit the blueprint, please go to the EDIT panel.')
		else:
			print(form.errors)
	context = {
		"form" : form
	}
	return render(request, 'add-floor.html', context)

def addRoutePageView(request):
	form = RouteCreateForm()
	if request.method == "POST":
		form = RouteCreateForm(request.POST)
		if form.is_valid():
			checkBuild = form.cleaned_data.get("buildID")
			checkDest = form.cleaned_data.get("destination")
			checkRoom = form.cleaned_data.get('roomNo')
			checkDir = form.cleaned_data.get("directions")
			if Routes.objects.filter(buildID=checkBuild, roomNo=checkRoom).exists():
				messages.error(request, 'Route already exists, if you want to edit route, please go to the EDIT panel.')
			else:
				try:
					Routes.objects.create(**form.cleaned_data)	
					messages.success(request, 'Successfully added route!')
					return HttpResponseRedirect('/add-route/')
				except IntegrityError as e:
					messages.error(request, 'Route already exists, if you want to edit route, please go to the EDIT panel.')
		else:
			print(form.errors)
	context = {
		"form" : form
	}
	return render(request, 'add-route.html', context)

def deleteFloorPageView(request):
	form = DeleteFloor()
	if request.method == "POST":
		form = DeleteFloor(request.POST)
		if form.is_valid():
			checkBuild = form.cleaned_data.get("buildID")
			checkFloor = form.cleaned_data.get("floorNo")
			try:
				floor = Floor.objects.get(buildID=checkBuild, floorNo=checkFloor)
				floor.delete()
				messages.success(request, 'Successfully deleted the blueprint!')
				return HttpResponseRedirect('/delete-floor/')
			except ObjectDoesNotExist:
				messages.error(request, 'Blueprint does not exist. If you want to add the blueprint, please go to the ADD panel.')
		else:
			print(form.errors)
	context = {
		"form" : form
	}
	return render(request, 'delete-floor.html', context)

def deleteRoutePageView(request):
	form = DeleteRoute()
	if request.method == "POST":
		form = DeleteRoute(request.POST)
		if form.is_valid():
			checkBuild = form.cleaned_data.get("buildID")
			checkFloor = form.cleaned_data.get("roomNo")
			try:
				floor = Routes.objects.get(buildID=checkBuild, roomNo=checkFloor)
				floor.delete()
				messages.success(request, 'Successfully deleted route!')
				return HttpResponseRedirect('/delete-floor/')
			except ObjectDoesNotExist:
				messages.error(request, 'Blueprint does not exist. If you want to add the blueprint, please go to the ADD panel.')
		else:
			print(form.errors)
	context = {
		"form" : form
	}
	return render(request, 'delete-route.html', context)

def editFloorPageView(request):
	#return render(request, "edit-floor.html")
	form = FloorCreateForm()
	if request.method == "POST":
		form = FloorCreateForm(request.POST)
		if form.is_valid():
			checkBuild = form.cleaned_data.get("buildID")
			checkFloor = form.cleaned_data.get("floorNo")
			checkLink = form.cleaned_data.get("floorImageLink")
			if Floor.objects.filter(buildID=checkBuild, floorNo=checkFloor).exists():
				try:
					Floor.objects.filter(buildID=checkBuild, floorNo=checkFloor).update(floorImageLink=checkLink)
					messages.success(request, 'Successfully updated the blueprint!')
					return HttpResponseRedirect('/edit-floor/')
				except ObjectDoesNotExist:
					messages.error(request, 'Blueprint does not exist. If you want to add the blueprint, please go to the ADD panel.')
			else:
					messages.error(request, 'Blueprint does not exist. If you want to add the blueprint, please go to the ADD panel.')
		else:
			print(form.errors)	
	context = {
		"form" : form
	}
	return render(request, 'edit-floor.html', context)

def editBuildingPageView(request):
	#return render(request, "edit-floor.html")
	form = EditBuilding()
	if request.method == "POST":
		form = EditBuilding(request.POST)
		if form.is_valid():
			checkBuild = form.cleaned_data.get("buildID")
			checkFloor = form.cleaned_data.get("buildFloors")
			if Building.objects.filter(buildName=checkBuild, buildExist=True).exists():
				try:
					Building.objects.filter(buildName=checkBuild).update(buildFloors=checkFloor)
					messages.success(request, 'Successfully updated the blueprint!')
					return HttpResponseRedirect('/edit-building/')
				except ObjectDoesNotExist:
					messages.error(request, 'Building does not exist. If you want to add the building, please go to the ADD panel.')
			else:
					messages.error(request, 'Building does not exist. If you want to add the building, please go to the ADD panel.')
		else:
			print(form.errors)	
	context = {
		"form" : form
	}
	return render(request, 'edit-building.html', context)

def deleteBuildingPageView(request):
	#return render(request, "edit-floor.html")
	form = DeleteBuilding()
	if request.method == "POST":
		form = DeleteBuilding(request.POST)
		if form.is_valid():
			checkBuild = form.cleaned_data.get("buildID")
			if Building.objects.filter(buildName=checkBuild, buildExist=True).exists():
				try:
					Building.objects.filter(buildName=checkBuild).update(buildExist=False)
					messages.success(request, 'Successfully delete the building!')
					return HttpResponseRedirect('/edit-building/')
				except ObjectDoesNotExist:
					messages.error(request, 'Building does not exist. If you want to add the building, please go to the ADD panel.')
			else:
					messages.error(request, 'Building does not exist. If you want to add the building, please go to the ADD panel.')
		else:
			print(form.errors)	
	context = {
		"form" : form
	}
	return render(request, 'delete-building.html', context)

def editRoutePageView(request):
	#return render(request, "edit-floor.html")
	form = RouteCreateForm()
	if request.method == "POST":
		form = RouteCreateForm(request.POST)
		if form.is_valid():
			checkBuild = form.cleaned_data.get("buildID")
			checkDest = form.cleaned_data.get("destination")
			checkRoom = form.cleaned_data.get('roomNo')
			checkDir = form.cleaned_data.get("directions")
			if Routes.objects.filter(buildID=checkBuild, roomNo=checkRoom).exists():
				try:
					Routes.objects.filter(buildID=checkBuild, roomNo=checkRoom).update(directions=checkDir, destination=checkDest)
					messages.success(request, 'Successfully updated route!')
					return HttpResponseRedirect('/edit-route/')
				except ObjectDoesNotExist:
					messages.error(request, 'Route does not exist. If you want to add route, please go to the ADD panel.')
			else:
					messages.error(request, 'Route does not exist. If you want to add route, please go to the ADD panel.')
		else:
			print(form.errors)	
	context = {
		"form" : form
	}
	return render(request, 'edit-route.html', context)

# view dcs.html
def dcsPageView(request):
	if Floor.objects.filter(buildID='dcs001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='dcs001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='dcs001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'dcs.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view engglib2.html
def enggLib2PageView(request):
	if Floor.objects.filter(buildID='engglib2001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='engglib2001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='engglib2001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'engglib2.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view coe.html
def coePageView(request):
	if Floor.objects.filter(buildID='coe001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='coe001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='coe001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'coe.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view  eee.html
def eeePageView(request):
	if Floor.objects.filter(buildID='eee001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='eee001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='eee001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'eee.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view ice.html
def icePageView(request):
	if Floor.objects.filter(buildID='ice001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='ice001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='ice001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'ice.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view mmm.html
def mmmPageView(request):
	if Floor.objects.filter(buildID='dmmme001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='dmmme001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='dmmme001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'mmm.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view che.html
def chePageView(request):
	if Floor.objects.filter(buildID='dche001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='dche001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='dche001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'che.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view ie.html
def iePageView(request):
	if Floor.objects.filter(buildID='dieor001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='dieor001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='dieor001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'ie.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')


# view ge.html
def gePageView(request):
	if Floor.objects.filter(buildID='dge001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='dge001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='dge001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'ge.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')


# view me.html
def mePageView(request):
	if Floor.objects.filter(buildID='dme001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='dme001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='dme001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'me.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')

# view nec.html
def necPageView(request):
	if Floor.objects.filter(buildID='nec001', floorNo=1).exists():
		try:
			getFloors = Floor.objects.filter(buildID='nec001')	# get all info inluding the floorImageLink
			dcsFloors = []
			getBuildings = Building.objects.all()
			for floors in getFloors:
				dcsFloors.append(floors.floorNo)	# list of the floorIDs for hecking
			getRoutes = Routes.objects.filter(buildID='nec001')
			#print(dcsFloors)
			#for x in dcsFloors:
			#	print(x.floorImageLink)
			return render(request, 'nec.html', {"dcsFloors" : dcsFloors, "getFloors" : getFloors, "getBuildings" : getBuildings, "getRoutes" : getRoutes})
		except:
			return render(request, 'error.html')
	else:
		return render(request, 'error.html')
