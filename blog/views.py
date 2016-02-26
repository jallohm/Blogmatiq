from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 

# Create your views here.
def home(request):
	return HttpResponse("Home of Blogmatiq :)")

def blogs(request):
	return HttpResponse("List of Blogs for user")


