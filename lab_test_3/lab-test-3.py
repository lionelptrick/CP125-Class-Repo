import csv

# Function 1: Calculate and display average height 
def read_bmi(input_file):
    bmi_file = open('input_file', 'r')
    reader_bmi = csv.reader(bmi_file)
    next(reader_bmi)

    total_height = 0
    count = 0 

    for row in reader_bmi:
        total_height += float(row[1])
        count += 1

        average_height = total_height / count

        print(f"Average height: {average_height}")
        
    bmi_file.close()

# Function 2: Input and Verify Data
def output_bmi(bmi_data):
    gender = input("Enter Gender: ")
    height = float(input("Enter Height: "))
    weight = float(input("Enter Weight: "))
    bmi_index = float(input("Enter BMI: "))

    data_file = open(bmi_data, 'a', newline='')
    writer = csv.writer(data_file)
    writer.writerow([gender, height, weight, bmi_index])
    data_file.close()

    verify_data = open(bmi_data, 'r')
    data_reader = csv.reader(verify_data)

    for row in data_reader:
        print(row)

    data_reader.close()
        
result = output_bmi('Users/User/CP125-Class-Repo/lab_test_3/bmi.csv')



