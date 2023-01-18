from django.shortcuts import render

# Create your views here.

from django.views.generic import View


class AdditionView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)
       
        return render(request,"add.html")

class SubstractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")

class MultiplicationView(View):
    def get(self,request,*args,**kw):
        return render(request,"mul.html")