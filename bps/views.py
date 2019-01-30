from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
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

@api_view(['GET', 'POST'])
def BuildingList(request):
    if request.method == 'GET':
        blue_print = Building.objects.all()
        serializer = BuildingSerializer(blue_print, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BuildingSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def FloorList(request):
    if request.method == 'GET':
        blue_print = Floor.objects.all()
        serializer = FloorSerializer(blue_print, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = FloorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)