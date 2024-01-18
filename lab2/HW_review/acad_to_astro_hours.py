# ----------------------------------- Task: ---------------------------------- #
# Given that:
# An astronomical hour consists of 60 minutes
# An academical hour consists of 40 minutes
# For each 3 academical hours there are 15 minutes brake
# Write a Python program, that will print out how many astronomical hours a python course should take, if it consists of 64 academical hours, including the respective brakes
# Try to think of a solution, which will be readable enough and easy to maintain in future
# Write your code in HW/acad_to_astro_hours.py file

# variables declaration
minutes_in_astro_hour = 60
minutes_in_acad_hour = 40
course_total_acad_hours = 64
acad_hours_in_a_day = 3
minutes_in_break = 15

# program logic:
course_days = course_total_acad_hours/acad_hours_in_a_day
total_breaks_minutes = course_days * minutes_in_break

total_course_minutes = course_total_acad_hours * minutes_in_acad_hour + total_breaks_minutes
total_course_astro_hours = total_course_minutes / minutes_in_astro_hour

print(f'Total course astronomical hours are: {total_course_astro_hours}')