from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'image']
        labels = {
            'name': 'Enter your name',
        }
        error_messages = {
            'name': {'required':'Write your name',},
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your name', 'id':'uniqueid'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'})
        }
    def clean_name(self):
        data = self.cleaned_data["name"]
        if len(data) < 4:
            return forms.ValidationError("Enter more than or equal 4 chars")
        return data
    