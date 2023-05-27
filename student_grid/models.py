from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Student(models.Model):
    gender_choices = (
        ('Male','Male'),
        ('Female','Female')
        )
    
    std_id = models.CharField(max_length=15, verbose_name="Student ID", unique=True)
    std_fname = models.CharField(max_length=50, verbose_name="First Name")
    std_lname = models.CharField(max_length=50, verbose_name="Last Name", default=None)
    dob = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Date of Birth")
    gender = models.CharField(verbose_name="Gender", choices=gender_choices, default='Male', max_length=10)
    max_total_marks = models.CharField(max_length=4, verbose_name="Maximum Total Marks")
    total_marks = models.CharField(max_length=4, verbose_name="Gained Total Marks")
    percentage = models.CharField(max_length=3, verbose_name="Percentage")

    REQUIRED_FIELDS = ['std_id','std_fname','dob','gender', 'max_total_marks','total_marks','percentage']

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.std_id

    # def get_absolute_url(self):
    #     return reverse("Student_detail", kwargs={"pk": self.pk})
