# Original data
students = [
    {"name": "Alice", "age": 20, "grade": 87, "major": "Physics"},
    {"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
    {"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
    {"name": "Diana", "age": 21, "grade": 92, "major": "Programming"}
]

for i in students:
    i["graduation_year"] = 2024

for i in students:
    if "age" in students:
        del i["age"]

print(students)
