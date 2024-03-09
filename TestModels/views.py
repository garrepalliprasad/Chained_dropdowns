from django.shortcuts import render
from .models import District,Mandal,Village
from django.http import JsonResponse
# Create your views here.

def index(request):
    districts=District.objects.all()
    context={'districts':districts}
    return render(request,'index.html',context)

def mandals(request):
    id=request.GET['id']
    mandals=Mandal.objects.filter(district_id=id).values('id','name')
    return JsonResponse(list(mandals),safe=False)

def villages(request):
    id=request.GET['id']
    villages=Village.objects.filter(mandal_id=id).values('id','name')
    return JsonResponse(list(villages),safe=False) 
