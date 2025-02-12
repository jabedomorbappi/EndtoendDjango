from django.shortcuts import render

from .forms import ContactForm,AnotherForm
from .models import Contact,AnotherModels



def contactview(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        content=request.POST.get('content')
        obj=Contact(name=name,phone=phone,content=content)
        obj.save()
        
    else:
        form=ContactForm()
    return render(request,'LearnForms/index.html',{"form":form})        
    
# Create your views here.

from django.shortcuts import render, redirect
from .forms import AnotherForm
from .models import AnotherModels  # Ensure you have imported the model

def anothercontactview(request):
    if request.method == "POST":
        form = AnotherForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            roll = form.cleaned_data['roll']
            address = form.cleaned_data['address']
            district = form.cleaned_data['district']
            country = form.cleaned_data['country']

            # Save to the database
            AnotherModels.objects.create(
                fname=fname, lname=lname, roll=roll,
                address=address, district=district, country=country
            )

            # Redirect to success page or same form page (avoiding resubmission on refresh)
            #return redirect('success_page')  # Change to your success page URL name
    else:
        form = AnotherForm()

    return render(request, 'LearnForms/anotherindex.html', {"form": form})
