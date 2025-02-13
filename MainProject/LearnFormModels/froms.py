from django import forms
from .models import StudentForm

class StudentForm(forms.ModelForm):
    """Form definition for Srudent."""

    class Meta:
        """Meta definition for Srudentform."""
        
        model = StudentForm
        fields = "__all__"

    