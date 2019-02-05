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
		entries = Building.objects.get(buildID='dcs001')
		return render(request, 'dcs.html')
	except:
		return render(request, 'error.html')

def coePageView(request):
	try:
		entries = Building.objects.get(buildID='coe001')
		return render(request, 'coe.html')
	except:
		return render(request, 'error.html')