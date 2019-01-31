from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def homePageView(request):
	#return HttpResponse('MaroonPrint')
	return render(request, 'home.html')

#class homePageView(TemplateView):
#	template = 'home.html'