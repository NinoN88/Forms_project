from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.author})"

