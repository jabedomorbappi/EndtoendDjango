from django.shortcuts import render

# Create your views here.
from .froms import StudentForm

def studentform(request):
    
    if request.method=="POST":
        form=StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    else:
        form=StudentForm()
        
    return render(request,'LearnFormModels/index.html',{'form':form})            
        