from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def  hom(request):
    return HttpResponse("shop home page")
def  products(request):
    return HttpResponse("blog product page")