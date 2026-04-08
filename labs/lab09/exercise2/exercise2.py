import pandas as pd

def compare_averages(filename):

    data = pd.read_csv(filename)

    mean_math = round(data['Math'].mean(), 1)
    mean_science = round(data['Science'].mean(), 1)
    mean_english = round(data['English'].mean(), 1)

    averages = {
        "Math": mean_math,
        "Science": mean_science,
        "English": mean_english
    }

    best_subject = max(averages, key=averages.get)
    worst_subject = min(averages, key=averages.get)

    averages['best_subject'] = best_subject
    averages['worst_subject'] = worst_subject

    return averages
    
    pass
