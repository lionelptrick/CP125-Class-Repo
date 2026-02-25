def get_student_courses(enrollments, student_id):
    """Return set of courses this student has completed."""
    courses = set()
    for sid, course in enrollments:
        if sid == student_id:
            courses.add(course)
    return courses
    pass

def find_missing_courses(completed_courses, required_courses):
    """Return set of required courses not yet completed."""
    return required_courses - completed_courses
    pass

def build_student_report(students, enrollments, required_courses):
    """Return sorted list of tuples (student_id, missing_count) for students with missing courses."""
    report = []

    for student in all_students:
        completed = get_student_courses(enrollments, student_id)
        missing = find_missing_courses(completed_courses, required_courses)

        if len(missing) > 0:
            report.append((student, len(missing)))

    return sorted(report, key=lambda x: x[1], reverse=True)
    
def find_incomplete_students(enrollments, required_courses):
    """Find students who haven't completed all required courses."""
    

    pass


