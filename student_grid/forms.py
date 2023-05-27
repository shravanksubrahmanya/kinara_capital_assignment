from django import forms

class StudentFilterForm(forms.Form):
    gender_choices = (
        ('Male','Male'),
        ('Female','Female')
        )
    
    std_id = forms.CharField(max_length=15, label="Student ID")
    std_fname = forms.CharField(max_length=50, label="First Name")
    std_lname = forms.CharField(max_length=50, label="Last Name")
    gender = forms.CharField(label="Gender", max_length=10)
    percentage = forms.CharField(max_length=3, label="Percentage")
