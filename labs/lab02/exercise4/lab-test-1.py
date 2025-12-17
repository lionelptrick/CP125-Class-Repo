# PROGRAMMER'S NAME: LIONEL ANAK PATRICK PAT
# PROBLEM DESCRIPTION: Write a Python programs that checks for one student by defining a function that called determine_grade which accepts a mark and returns a grade.

def determine_grade(mark):

    if mark >= 80:
        return "A"
    elif mark >= 60 and mark <= 79:
        return "B"
    elif mark >= 50 and mark <= 59:
        return "C"
    elif mark >= 40 and mark <= 49:
        return "D"
    else:
        return "F"
    

mark = float(input("Enter the student's mark: "))
grade = determine_grade(mark)  

print(f"Mark: {mark}, Grade: {grade}")