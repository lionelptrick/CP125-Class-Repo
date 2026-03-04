def generate_enrollment_report(old_file, new_file, output_file):
    f_old = open(old_file, 'r')
    old_students = f_old.read().splitlines()
    f_old.close()
    
    f_new = open(new_file, 'r')
    new_students = f_new.read().splitlines()
    f_new.close()
    
    all_students = set(old_students + new_students)
    sorted_students = sorted(all_students)
    
    f_out = open(output_file, 'w')
    for student in sorted_students:
        f_out.write(student + '\n')
    f_out.close()
