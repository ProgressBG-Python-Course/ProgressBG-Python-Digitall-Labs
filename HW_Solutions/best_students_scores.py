### Task1: create best_students_scores dictionary with "students:scores" pairs, where scores>4.0:

student_scores = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "Georgy": 5.00,
}

# # Solution with loop - not Pythonic
# best_students_scores = {}
# for student, score in student_scores.items():
#     if( score > 4.00):
#       best_students_scores[student] = score

# # Solution with comprehension:
# best_students_scores = {k:v for k,v in student_scores.items() if v>4.0}

# print(best_students_scores)


### Task 2: Print out the name and score of the student with maximum score

# Solution with dictionaries:
# student_scores = {
#     "Ivan": 5.00,
#     "Alex": 3.50,
#     "Maria": 5.50,
#     "Georgy": 5.00,
# }

# max_score = max(student_scores.values())
# best_student = {k:v for k,v in student_scores.items() if v==max_score}

# print(best_student)

# # Solution with list of tupples:
student_scores = [
    ("Ivan", 5.00),
    ("Alex", 3.50),
    ("Maria", 5.50),
    ("Georgy", 5.00)
]
# print(list(enumerate(student_scores)))

# # using loops:
max_score = 0
max_idx = 0

for idx, student in enumerate(student_scores):
    if student[1]>max_score:
        max_score = student[1]
        max_idx = idx

print(student_scores[max_idx])

# using sorted: Imlement after lamda topic


