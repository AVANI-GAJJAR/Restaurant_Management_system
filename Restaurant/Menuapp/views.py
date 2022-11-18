from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from Menuapp.models import Table
# Create your views here.
def index(request):
    mymembers = Table.objects.all().values()
    template = loader.get_template('index.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
    #return render(request,'index.html',content)
    #return HttpResponse("Hello :>")
def add(request):
    return render(request,'add.html')
    #return HttpResponse("Hello add:>")
def addrecord(request):
    nm=request.POST['name']
    pr=request.POST['price']
    qty=request.POST['quantity']
    m=Table(name=nm,price=pr,quantity=qty)
    m.save()
    return HttpResponse("Added")
def show(request):
    return HttpResponse("Hello show:>")
def update(request,id):
    mymember = Table.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello update:>")
def updaterecord(request,id):
  nm=request.POST['name']
  pr=request.POST['price']
  qty=request.POST['quantity']
  member = Table.objects.get(id=id)
  member.name = nm
  member.price = pr
  member.quantity = qty
  member.save()
  return HttpResponseRedirect(reverse('index'))
def delete(request,id):
    member =Table.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))