import pandas as pd

def explore_data(filename):

    data = pd.read_csv(filename)

    total_students = len(data)
    subjects = ['Math', 'Science', 'English']
    math_average = round(data[' Math'].mean(), 1)
    highest_math_students = data.loc[data['Math'].max(), 'Name']
    
    return {
        "total_students": total_students,
        "subjects": subjects,
        "math_average": math_average,
        "highest_math_student": highest_math_students 
    }
    pass
