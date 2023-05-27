import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','kinara_capital_assignment.settings')

import django
django.setup()

# Fake population script
import random
from student_grid.models import Student
from faker import Faker

fake = Faker()

def populate(N = 50):

    for entry in range(N):
        student_id = fake.random_number(digits=8)
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=22)
        gender = random.choice(['Male', 'Female'])
        maximum_total_marks = random.randint(500, 1000)
        gained_total_marks = random.randint(0, maximum_total_marks)
        percentage = round((gained_total_marks / maximum_total_marks) * 100,2)

        std = Student.objects.get_or_create(std_id = student_id, 
                                            std_fname = first_name,
                                            std_lname = last_name,
                                            dob = date_of_birth,
                                            gender = gender,
                                            max_total_marks = maximum_total_marks,
                                            total_marks = gained_total_marks,
                                            percentage = percentage)[0]

if __name__ == '__main__':
    print("Populating student database.....")
    populate(N = 100)
    print("Populating complete!")