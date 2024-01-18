mport math

ACADEMIC_HOUR = 40
ASTRONOMICAL_HOUR = 60
BREAK = 15
TOTAL_HOURS = 64

# Total number of astronomical hours of breaks
total_breaks = ((math.floor((TOTAL_HOURS/3)))*15)/ASTRONOMICAL_HOUR
#Total number of astronomical hours of academic hours
total_course_hours = (ACADEMIC_HOUR*TOTAL_HOURS)/ASTRONOMICAL_HOUR


print(total_breaks + total_course_hours)