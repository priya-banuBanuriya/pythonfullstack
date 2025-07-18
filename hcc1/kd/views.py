# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import dbCon
def add (request):
    return render(request,'add.html')
def addsave (request):
    name=request.GET["name"]
    regno = request.GET["regno"]
    department = request.GET["department"]
    mail = request.GET["mail"]
    d={
            'name':name,
            'regno':regno,
            'dept':department,
            'mail':mail
    }
    dbCon.col.insert_one(d)
    return redirect('listdata')
def listdata(request):
    dt=list(dbCon.col.find())
    return render (request,'list.html',{'var':dt})
def edit(request,regno):
    entry=dbCon.col.find_one({"regno":regno})
    if request.method=="POST":
        name=request.POST["name"]
        department= request.POST["department"]
        mail= request.POST["mail"]
        dbCon.col.update_one(
            {"regno":regno},
            {"$set":{
              "name":name,
              "dept":department,
              "mail":mail
            }}
        )
        return redirect('listdata')
    return render(request,"edit.html",{"entry":entry})
def delete (request,regno):
    entry=dbCon.col.find_one({"regno":regno})
    dbCon.col.delete_one({"regno":regno})
    return redirect('listdata')