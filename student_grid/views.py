from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.utils import timezone
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# models
from student_grid.models import Student

class StudentListView(ListView):
    model = Student
    template_name = "index.html"
    queryset = Student.objects.all()
    context_object_name = 'student_list'
    paginate_by = 10

    def get_paginate_by(self, queryset):
        num_records = self.request.GET.get('no_of_rows')
        if num_records:
            print("Hi")
            try:
                return int(num_records)
            except ValueError:
                pass

        return self.paginate_by
    
    def get_queryset(self):
        # queryset = super().get_queryset()
        student_id = self.request.GET.get('student_id')
        fname = self.request.GET.get('fname')
        lname = self.request.GET.get('lname')
        gender = self.request.GET.get('gender')
        minpercentage = self.request.GET.get('minpercentage')
        maxpercentage = self.request.GET.get('maxpercentage')
        # self.paginate_by = self.request.GET.get('no_of_rows')

        if student_id:
            self.queryset = self.queryset.filter(std_id=student_id)

        if fname:
            self.queryset = self.queryset.filter(std_fname__icontains=fname)
        
        if lname:
            self.queryset = self.queryset.filter(std_lname__icontains=lname)
        
        if gender:
            self.queryset = self.queryset.filter(gender=gender)
        
        if minpercentage:
            self.queryset = self.queryset.filter(percentage__gt=minpercentage)
        
        if maxpercentage:
            self.queryset = self.queryset.filter(percentage__lt=maxpercentage)

        return self.queryset
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     paginator = Paginator(context['student_list'], self.paginate_by)
    #     page_number = self.request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #     context['page_obj'] = page_obj
    #     return context

