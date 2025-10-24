from django.shortcuts import render, redirect
from .forms import StudentForm, StudentModelForm
from .models import Student, Course

def home_view(request):
    return render(request, 'home.html')

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            course_title = form.cleaned_data['course']
            course, created = Course.objects.get_or_create(title=course_title)
            Student.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                course=course
            )
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_modelform_view(request):
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentModelForm()
    return render(request, 'student_modelform.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')



