from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.utils import timezone
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# models
from student_grid.models import Student

# forms
from student_grid.forms import StudentFilterForm

class StudentListView(ListView):
    model = Student
    template_name = "index.html"

    def get_queryset(self):
        queryset = Student.objects.all()
        student_id = self.request.GET.get('student_id')
        fname = self.request.GET.get('fname')
        lname = self.request.GET.get('lname')
        gender = self.request.GET.get('gender')
        minpercentage = self.request.GET.get('minpercentage')
        maxpercentage = self.request.GET.get('maxpercentage')

        if student_id:
            queryset = queryset.filter(std_id=student_id)

        if fname:
            queryset = queryset.filter(std_fname__icontains=fname)
        
        if lname:
            queryset = queryset.filter(std_lname__icontains=lname)
        
        if gender:
            queryset = queryset.filter(gender=gender)
        
        if minpercentage:
            queryset = queryset.filter(percentage__gt=minpercentage)
        
        if maxpercentage:
            queryset = queryset.filter(percentage__lt=maxpercentage)

        return queryset
    

#  std_id = models.CharField(max_length=15, verbose_name="Student ID", unique=True)
#     std_fname = models.CharField(max_length=50, verbose_name="First Name")
#     std_lname = models.CharField(max_length=50, verbose_name="Last Name", default=None)
#     dob = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Date of Birth")
#     gender = models.CharField(verbose_name="Gender", choices=gender_choices, default='Male', max_length=10)
#     max_total_marks = models.CharField(max_length=4, verbose_name="Maximum Total Marks")
#     total_marks = models.CharField(max_length=4, verbose_name="Gained Total Marks")
#     percentage = models.

