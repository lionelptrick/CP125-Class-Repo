# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv 

def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.

    Args:
        input_file: path to sales CSV (product,quantity,price)
        output_file: path to output text file

    Returns:
        tuple: (total, average, highest, lowest)
    """
    # TODO: Implement this function
    pass
    sales_file = open(input_file, 'r', newline='')
    sales_reader = csv.reader(sales_file)
    next(sales_reader)

    revenue_file = open(output_file, 'w', newline='')
    revenue_writer = csv.writer(revenue_file)

    total = 0
    count = 0
    average = 0
    highest = 0
    lowest = None

    for row in sales_reader:
        product = row[0]
        quantity = float(row[1])
        price = float(row[2])

        revenue = quantity * price

        total += revenue
        count += 1

        if revenue > highest:
            highest = revenue

        if lowest is None or revenue < lowest:
            lowest = revenue 

    average = total/count

    revenue_file.write(f"Total Revenue: ${total:.2f}\n")
    revenue_file.write(f"Average Revenue: ${average:.2f}\n")
    revenue_file.write(f"Highest Revenue: ${highest:.2f}\n")
    revenue_file.write(f"Lowest Revenue: ${lowest:.2f}\n")

    sales_file.close()
    revenue_file.close()

    return (total, average, highest, lowest)

# Test your code here
result = summarize_sales("labs/lab08/exercise5/data/sales.csv", "labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
