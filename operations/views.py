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
       
        return render(request,"add.html",{"out":result})

class SubstractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        return render(request,"sub.html",{"res":result})

class MultiplicationView(View):
    def get(self,request,*args,**kw):
        return render(request,"mul.html")

from functools import reduce
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwrgs):
        n=int(request.POST.get("num"))
        fact=reduce(lambda n1,n2:n1*n2,range(1,(n+1)))
        
        return render(request,"fact.html",{"result":fact})


class PrimeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num")) #8 

        flg=any([n % i==0 for i in range(2,n)])
       
        isPrime="not prime" if flg else "prime"
        
        
        return render(request,"prime.html",{"out":isPrime})
        

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")