from django.shortcuts import render

from django.http import HttpResponse
from Mazolutions.data import *

# Create your views here.
def index(request):
    return HttpResponse("find the right mazolutions, wow!")


    
