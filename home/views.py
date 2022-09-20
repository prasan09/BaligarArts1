from multiprocessing import context
from sre_parse import State
from tokenize import Name
from django.shortcuts import render, HttpResponse
from home.models import Order1
# Create your views here.
def index(request):
    return render (request, 'index.html')
    #return HttpResponse("This is homepage")
    


def aboutme(request):
    return render (request, 'aboutme.html')
def creation(request):
    return render (request, 'creation.html')
def custom(request):
    return render (request, 'custom.html')
def signup(request):
    return render (request, 'signup.html')
def Order(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        vname = request.POST.get("vname")
        xname = request.POST.get("xname")
        yname = request.POST.get("yname")
        ins = Order1(name=uname,address= vname, pincode=xname, state=yname)
        ins.save()

    return HttpResponse("<h1>Order Placed Succesfully</h1>")




