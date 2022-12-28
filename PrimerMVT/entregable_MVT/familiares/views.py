from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiares

def create_familiar(request):
    Familiares.objects.create(name='Justo',birth_year=2011,zodiac_sign='acuario',is_adult=False)
    return HttpResponse('familiar creado')

def list_familiares(request):
    all_familiares=Familiares.objects.all()
    context={'familiares':all_familiares,}
    return render(request,'list_familiares.html',context=context)
# Create your views here.
