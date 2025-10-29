from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('form/', views.student_form_view, name='student_form'),
    path('modelform/', views.student_modelform_view, name='student_modelform'),
    path('success/', views.success_view, name='success'),

    # 📚 CRUD ბმულები
    path('books/', views.book_list_create, name='book_list_create'),
    path('books/update/<int:pk>/', views.book_update, name='book_update'),
    path('books/delete/<int:pk>/', views.book_delete, name='book_delete'),
]

