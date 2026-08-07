import json
from modules.products import find_product, save_products
from modules.customers import  find_customer, save_customers


def load_sales():
    try:
        with open("data/sales.json", "r") as file:
            sales = json.load(file)
            return sales
    except FileNotFoundError:
        return []

def save_sales(sales):
    try:
        with open("data/sales.json", "w") as file:
            json.dump(sales, file, indent=4)
    except Exception as e:
        print(f"Error saving sales {e}")

def generate_sale_id(sales):
    if sales:
        return max(sale["id"] for sale in sales) +1
    else:
        return 1
        
# sales = []
sales = load_sales()
        
def sell_product(products, customers, sales):
    product_ID = int(input("Enter the ID of the product you want to sell: "))
    quantity = int(input("Enter the quantity of the product to sell: "))
    customer_id = int(input("Enter the customer ID: "))
    
    customer =  find_customer(customers , customer_id)
    product = find_product(products,product_ID)
    
    if product:
        if quantity <= product["quantity"]:
            product["quantity"] -= quantity
            new_sale = {
                "id": generate_sale_id(sales),
                "Customer_id": customer["id"],
                "product": product["name"], 
                "price": product["price"], 
                "quantity": quantity, 
                "total": product["price"]* quantity
            }
            sales.append(new_sale)
            save_products(products)
            save_sales(sales)
            print("Sale completed successfully")
        else:
            print("Not enough stock!")
    else:
        print("product not found")

def view_sales(sales):
    print("----------Sales-----------")
    for sale in sales:
        print(f"id: {sale['id']}")
        print(f"Name: {sale['product']}")
        print(f"Price: R {sale['price']:.2f}")
        print(f"Quantity: {sale['quantity']}")
        print(f"Total: R {sale['total']:.2f}")
        print("-" *20)