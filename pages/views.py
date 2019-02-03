from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render_to_response

# Create your views here.
def homePageView(request):
	#return HttpResponse('MaroonPrint')
	return render(request, 'home.html')

def dcsPageView(request):
	try:
		blue_print = Building.objects.get(buildID = 'coe0001')
	except Building.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)
	return render(request, 'coe.html')