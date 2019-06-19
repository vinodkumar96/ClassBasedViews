from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class getinput (View):
    def get (self,request):
        return render(request,"getinput.html")
class postinput (View):
    def get (self,request):
        return render(request,"postinput.html")
class add (View):
    def get (self,request):
        try:
            a=request.GET["t1"]
            b=request.GET["t2"]
            c=int(a)
            d=int(b)
            e=c+d
            return HttpResponse("the sum is:" +str(e))
        except(ValueError):
            return HttpResponse("Invalid Input")
    def post (self,request):
        try:
            a=request.POST["t1"]
            b=request.POST["t2"]
            c=int(a)
            d=int(b)
            e=c+d
            return HttpResponse("the sum is: " +str(e))
        except(ValueError):
            return HttpResponse("Invalid Input")
