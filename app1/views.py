from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('Heloo this is testing')
def AboutFun(request):
    return HttpResponse('<h1>this is about</h1>')
def hiiiFun(request):
    return HttpResponse('welcome')
def indexFun(request):
    return render(request,'index.html')
