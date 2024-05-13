from djiangi.http import HttpResponse
from django.shortcuts import redirect

def index(requesr):
	return HttpResponse("index")

def login(request):
	return redirect("/index')
