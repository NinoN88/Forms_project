from django.shortcuts import render, redirect
from .forms import StudentForm, StudentModelForm
from .models import Student, Course
from django.contrib import messages


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

from .forms import BookForm
from .models import Book



# 📘 Book List + Create (C და R)
def book_list_create(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ წიგნი წარმატებით დაემატა!")
            return redirect('book_list_create')
    else:
        form = BookForm()

    return render(request, 'book_list.html', {'form': form, 'books': books})


# ✏️ Update (U)
def book_update(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.info(request, "✏️ ცვლილებები შენახულია!")
            return redirect('book_list_create')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_update.html', {'form': form, 'book': book})


# ❌ Delete (D)
def book_delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    messages.warning(request, "❌ წიგნი წაიშალა.")
    return redirect('book_list_create')

