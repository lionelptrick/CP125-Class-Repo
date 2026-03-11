# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    # TODO: Implement this function.
    price_dictionary = {}

    products = open(products_file, 'r', newline='')
    orders = open(order_file, 'r', newline='')
    totalcost = open(output_file, 'w', newline='')

    product_reader = csv.reader(products)
    next(product_reader)

    for row in product_reader:
        product_id = row[0]
        price = float(row[2]) 
        price_dictionary[product_id] = price

    writer = csv.writer(totalcost)
    writer.writerow(['product_id', 'total_cost'])

    orders_reader = csv.reader(orders)
    next(orders_reader)

    grand_total = 0

    for row in orders_reader:
        product_id = row[0]
        quantity = int(row[1])

        total = price_dictionary[product_id] * quantity
        grand_total += total

        writer.writerow([product_id, f"{total:.2f}"])

    products.close()
    orders.close()
    totalcost.close()

    return grand_total

    pass


# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
