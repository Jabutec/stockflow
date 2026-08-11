def find_product(products, product_ID):
    for product in products:
        if product_ID == product["id"]:
            return product
    return None

def find_customer(customers, customer_id):
    for customer in customers:
        if customer_id == customer["id"]:
            return customer
    return None