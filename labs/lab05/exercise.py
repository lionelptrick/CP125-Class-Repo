# A list of student records
# Each record is (name, score, attendance_percent)
students = (
    ("Ali", 85, 95),
    ("Sara", 92, 98),
    ("Ahmad", 78, 80)
)

# Accessing nested data
first_student = students[0]
print(first_student)        # ("Ali", 85, 95)
print(first_student[0])     # "Ali"

# Or using unpacking in a loop (preferred)
for name, score, attendance in students:
    if attendance < 90:
        print(f"Warning: {name} has low attendance")