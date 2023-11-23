# from datetime import date
# from background_task import background
# from .models import Birthdays
# from franchise.models import Students

# @background(schedule=60*60*24)  # Schedule the task to run every 6 hours (adjust as needed)
# def check_and_add_birthdays():
#     print("func called")
#     today = date.today()
#     students_with_birthdays = Students.objects.filter(dob__day=today.day, dob__month=today.month)
#     print(students_with_birthdays)

#     for student in students_with_birthdays: 
#         Birthdays.objects.create(name=student.name,birthday=student.dob, franchise=student.franchise)
