def filter_products(products, preferred_categories, blocked_brands):
    filtered = []

    for product_name, details in products.items():
        category = details["category"]
        brand = details["brand"]

        if category in preferred_categories and brand not in blocked_brands:
            filtered.append(product_name)

    return filtered

products = {
    "iPhone": {"category": "Electronics", "brand": "Apple"},
    "Galaxy": {"category": "Electronics", "brand": "Samsung"},
    "Shirt": {"category": "Clothing", "brand": "Nike"}
}
preferred_categories = {"Electronics"}
blocked_brands = {"Apple"}
print(filter_products(products, preferred_categories, blocked_brands))