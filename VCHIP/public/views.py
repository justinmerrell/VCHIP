from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import CustomText

import random

def scanner(request):
    '''
    URL: /
    Method: GET
    This is the landing page of the app that sets up the environment.
    '''
    return render(request, 'landing_page.html', {'randid':random.randint(1000000000,9999999999)})

def code(request, code):
	print(code)
	try:
		customFields = CustomText.objects.get(tag=code)
		return render(request, 'landing_page.html', {'name': customFields.target_name, 'extra':customFields.target_extra, 'randid':random.randint(1000000000,9999999999)})

	except Exception as e:
		return render(request, 'landing_page.html', {'randid':random.randint(1000000000,9999999999)})

@csrf_exempt
def GenerateLink(request):
	print(request)
	print(request.POST)
	NewLink = CustomText.objects.create(target_name = request.POST.get('target_name'), target_extra = request.POST.get('extra_details'))
	NewLink.save()
	Link = CustomText.objects.get(id=NewLink.id)
	return HttpResponse(f"https://vchip.app/{Link.tag}/")
