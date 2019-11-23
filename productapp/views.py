from django.shortcuts import render
from . models import Product
def search(request):
    x=request.GET['pcat']
    y=request.GET['pname']
    recs=Product.objects.filter(pcat=x,pname=y)
    return render(request,'products.html',{'recs':recs})

def search1(request):
    x=request.GET['pcat']
    y=request.GET['pname']
    recs=Product.objects.filter(pcat=x,pname=y)
    return render(request,'product1.html',{'recs':recs})
