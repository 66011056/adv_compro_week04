students = [
    {"name": "Alice", "age": 20, "grade": 85, "major": "Physics"},
    {"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
    {"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
    {"name": "Diana", "age": 21, "grade": 92, "major": "Biology"}
]

for i in range(len(students)):
    if students[i]["name"] == "Alice":
        students[i]["grade"] = 87

for i in range(len(students)):
    if students[i]["name"] == "Diana":
        students[i]["major"] = "Programming"

print(students)
