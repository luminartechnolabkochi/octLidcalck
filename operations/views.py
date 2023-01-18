from django.shortcuts import render

# Create your views here.

from django.views.generic import View


class AdditionView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    def post(self,request,*args,**kwargs):
        print("hello there!!!!!")
        return render(request,"add.html")

class SubstractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")

class MultiplicationView(View):
    def get(self,request,*args,**kw):
        return render(request,"mul.html")