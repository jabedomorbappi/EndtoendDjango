from django.shortcuts import render,HttpResponse

from tution.models import Contact
def home(request):
    
    if request.method=="POST":
        name=['Rahul','Rohit','Raj']
    else:
        name=["this is get method",'Rahul','Rohit','Raj']    
    context={
        "name":name
    }
    return render(request,'home.html',context) 

def about(request):
    number=[x for x in range(1,100)]
    context={
        "number":number}
    return render(request,'about.html',context)
def information(request):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        
        obj=Contact(name=name,email=email,phone=phone)
        obj.save()
        
    return render(request,'info.html')