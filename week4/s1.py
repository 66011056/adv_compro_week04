# students = [
#     {"students_id": 1, "grade": 90},
#     {"students_id": 2, "grade": 75},
#     {"students_id": 3, "grade": 86},
#     {"students_id": 4, "grade": 60},
#     {"students_id": 5, "grade": 90},
# ]
# criteria = lambda student: True if student["grade"] > 80 else False
# filtered_students = list(filter(criteria, students))
# # Samilar to
# # filtered_students = [student for student in students if criteria(student)]
# print(students)
# print(students, filtered_students)

def greet(name):
    return f"Hi, {name}"