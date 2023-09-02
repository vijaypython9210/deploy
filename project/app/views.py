from django.shortcuts import render,HttpResponse
from . forms import MyForm
from . models import start

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            form.save()
            sam=start.objects.all().values()
            return render(request,"home.html")
        else:
            return HttpResponse('Data Already exists')
    else:
        form=MyForm()
    return render(request,'signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        sam=start.objects.filter(name=request.POST['name'],age__gt=18).values()
        return render(request,'result.html',{'sam':sam})
    else:
        return render(request,'login.html')

def showdata(request):
    sam=start.objects.all().values()
    return render(request,'result.html',{'sam':sam})