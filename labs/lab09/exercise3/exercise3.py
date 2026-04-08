import pandas as pd
import matplotlib.pyplot as plt

def show_math_trend(filename):

    df = pd.read_csv(filename)

    plt.plot(df.index, df['Math'], marker = 'o', linestyle = '-')
    plt.xlabel('Student Index')
    plt.ylabel('Math score')
    plt.title('Math Score Trends')
    plt.grid(True)

    plt.show()

    return len(df)

count = show_math_trend("labs/lab09/data/students.csv")

print(count)  # 25  


pass
