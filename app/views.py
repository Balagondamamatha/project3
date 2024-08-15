from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def starbucks(request):
    return HttpResponse('worst chai is available in starbucks')

def chocolate(request):
    return HttpResponse('chocolate is so delicious')
