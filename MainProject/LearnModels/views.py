from django.shortcuts import render
from .models import Employee,Students,Unique_Student

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





from django.shortcuts import render, redirect
from .forms import StudentForm

def student_registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('LearnModels:success_page')  # Redirect after successful submission
    else:
        form = StudentForm()

    return render(request, 'LearnModels/students.html', {'form': form})


from django.shortcuts import render

def success_page(request):
    return render(request, 'LearnModels/success.html')
