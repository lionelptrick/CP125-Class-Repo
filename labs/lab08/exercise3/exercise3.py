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
    for row in product_reader:
        product_reader[row['product_id']] =  float(row['price'])

    orders_reader = csv.reader(orders)
    for row in orders_reader:
        product_id = row['product_id']
        quantity = int(row['quantity'])

        total = price_dictionary[product_id] * quantity
        grand_total += total

    writer = csv.writer(totalcost)
    writer.writerow(['product_id', 'total_cost'])

    for 



    pass


# Test your code here
result = calculate_order_total("data/products.csv", "data/order.csv", "data/total.csv")
print(f"Grand total: ${result:.2f}")
