from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from productapp.models import Stock, Product,Cart
@login_required
def addcart(request):
    x=request.GET["pid"]
    qt=Stock.objects.filter(pid=x)
    qtt=0
    for p in qt:
         #global qtt
         qtt=p
    qt=[q for q in range(1,qtt.tot_qty+1)]
    return render(request,'addcart.html',{"pid":x,"qtt":qt})
def insertcart(request):
    x=request.GET["pid"]
    qt=int(request.GET["qt"])
    user=User.objects.get(id=request.session.get("_auth_user_id"))
    stc=Stock.objects.get(pid=int(request.GET["pid"]))
    stc.tot_qty=stc.tot_qty-int(qt)
    stc.save()
    un=str(user.username)
    pr=Product.objects.get(pid=int(x))
    a=int(str(x))
    b=int(str(qt))
    c=un
    d=float(pr.pcost)
    e=int(str(qt))*float(pr.pcost)
    f=pr.photo
    ct=Cart(username=c,pid=a,units=b,unitprice=d,tuprice=e,photo=f)
    ct.save()
    return render(request,'insertcart.html')
@login_required()
def cartview(request):
    # user=User.objects.filter(id=request.session.get("_auth_user_id"))
    # un=str(user.uname)
    # recs=Cart.objects.filter(username=un)
    recs=Cart.objects.all()
    return render(request,"cartdisplay.html", {'records':recs})
def display(request):
    user=User.objects.get(id=request.session.get("_auth_user_id"))
    un=str(user.username)
    recs=Cart.objects.filter(username=un)
    return recs
def delete(request):
    cs=Cart.objects.filter(id=int(request.GET["id"]))
    stc = Stock.objects.get(pid=int(request.GET["pid"]))
    ut=request.GET["units"]
    stc.tot_qty = stc.tot_qty + int(ut)
    stc.save()
    cs.delete()
    # return render(request,'cartdisplay.html',{'recs':display(request)})
    return cartview(request)
def modifycart(request):
    cid = request.GET["id"]
    x=(request.GET["pid"])
    qt=Stock.objects.filter(pid=x)
    qtt=0
    for p in qt:
        qtt=p
    qt=[q for q in range(1, qtt.tot_qty+1)]
    oldqt=request.GET['tot_qty']
    return render(request,'modifyqty.html',{"cartid":cid,"pid":x,"qtt":qt,"oqt":oldqt})
def modifiedcart(request):
    cid=int(request.GET["id"])
    nqt=int(request.GET["nqt"])
    stc=Stock.objects.get(pid=int(request.GET["pid"]))
    stc.tot_qty=int(stc.tot_qty)-nqt+int(request.GET["tot_qty"])
    stc.save()
    obj = Cart.objects.get(id=cid)
    obj.units=nqt
    up=obj.unitprice
    obj.tuprice=up*nqt
    obj.save()
    recs = Cart.objects.all()
    return render(request,"cartdisplay.html",{'records':recs})

