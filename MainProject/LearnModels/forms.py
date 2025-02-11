from django import forms
from .models import Unique_Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Unique_Student
        fields = ['fname', 'lname', 'roll_number', 'email', 'phone', 'course']

    def clean_roll_number(self):
        roll_number = self.cleaned_data.get('roll_number')
        if Unique_Student.objects.filter(roll_number=roll_number).exists():
            raise forms.ValidationError("This roll number already exists. Please enter a unique roll number.")
        return roll_number
