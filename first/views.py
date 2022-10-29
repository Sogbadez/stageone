import http
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse
from .models import Me
from .serializer import MeSerializer



def greet (response):
    return HttpResponse('Hello TheMustaeenah')

def me_intro(request):
    people=Me.objects.all()
    serializer=MeSerializer(people,many=True)
    return JsonResponse(serializer.data,safe=False)
