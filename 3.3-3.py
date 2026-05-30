student = {
    "name": "Alice",
    "age": "20",
    "grade": "A"
}

print("keys:",student.keys())
print("values:",student.values())

student["city"] = "Delhi"

student["age"] = "21"

del student["grade"]

print(student)