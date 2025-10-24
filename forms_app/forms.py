from django import forms
from .models import Student


class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    course = forms.CharField(max_length=100)

# მოდელზე დაფუძნებული ფორმა
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']
