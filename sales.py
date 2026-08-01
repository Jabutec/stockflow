import json
from products import find_product, save_products


def load_sales():
    try:
        with open("sales.json", "r") as file:
            sales = json.load(file)
            return sales
    except FileNotFoundError:
        return []

def save_sales(sales):
    try:
        with open("sales.json", "w") as file:
            json.dump(sales, file, indent=4)
    except Exception as e:
        print(f"Error saving sales {e}")
        
# sales = []
sales = load_sales()
        
def sell_product(products,sales):
    name = input("Enter the name of the product you want to sell: ").strip()
    quantity = int(input("Enter the quantity of the product to sell: ").strip())
    
    product = find_product(products,name)
    if product:
        if quantity <= product["quantity"]:
            product["quantity"] -= quantity
            new_sale = {
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
        print(f"Name: {sale['product']}")
        print(f"Price: R {sale['price']:.2f}")
        print(f"Quantity: {sale['quantity']}")
        print(f"Total: R {sale['total']:.2f}")
        print("-" *20)