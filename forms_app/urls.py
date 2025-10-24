from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # ← ეს ხაზია მთავარი ბმული
    path('form/', views.student_form_view, name='student_form'),
    path('modelform/', views.student_modelform_view, name='student_modelform'),
    path('success/', views.success_view, name='success'),
]

