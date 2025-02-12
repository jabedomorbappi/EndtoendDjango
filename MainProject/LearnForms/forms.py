from django import forms


class ContactForm(forms.Form):
    name=forms.CharField(max_length=100,label="your name")
    phone=forms.CharField(max_length=100,label="your phone")
    content=forms.CharField(max_length=100,label="your details")
    


class AnotherForm(forms.Form):
    fname=forms.CharField(max_length=100,label="your name")
    lname=forms.CharField(max_length=100,label="your last name")
    roll=forms.IntegerField(label="your roll")
    address=forms.CharField(max_length=100,label="your address")
    district=forms.CharField(max_length=100,label="your district")
    country=forms.CharField(max_length=100,label="your country")
    
    
    
    