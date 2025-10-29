from django import forms
from .models import Student, Book

# ჩვეულებრივი ფორმა
class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    course = forms.CharField(max_length=100)

# მოდელზე დაფუძნებული ფორმა (Student)
class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'course']

# მოდელზე დაფუძნებული ფორმა (Book)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year']


