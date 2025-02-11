from django.shortcuts import render
from .models import Employee,Students

def showLearnmodels(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        mob=request.POST['mob']
        job=request.POST['job']
        
        new_obj=Students(fname=fname,lname=lname,mob=mob,job=job)
        new_obj.save()
    return render(request, 'LearnModels/index.html')

def showSecond(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        mob=request.POST['mob']
        job=request.POST['job']
        
        new_obj=Employee(fname=fname,lname=lname,mob=mob,job=job)
        new_obj.save()
    return render(request, 'LearnModels/second.html')