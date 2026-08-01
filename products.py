import json


def load_products():
    try:
        with open("products.json", "r") as file:
            products = json.load(file)
            return products
    except FileNotFoundError:
        return []

def save_products(products):
    try:
        with open("products.json", "w") as file:
            json.dump(products, file, indent=4)
    except Exception as e:
        print(f"Error saving product{e}")
    
    
products = load_products()

    
    
# products = [
#     {"name" : "milk", "price": 20.00, "quantity": 50, "category": "dairy"},
#     {"name" : "Bread", "price": 22.25, "quantity": 25, "category": "bakery"},
#     {"name" : "popcorn", "price": 15.00, "quantity": 100, "category": "snacks"},
#     {"name" : "juice", "price": 18.00, "quantity": 70, "category": "beverages"},
# ]

def add_product(products):
    product_name = input("Enter the name of product: ").strip().lower()
    price = float(input("Enter the price of the product: ").strip())
    quantity = int(input("Enter the number of products: "))
    category = input("Enter the category of the product: ").strip().lower()
    
    new_product = {"name" : product_name, "price": price, "quantity": quantity, "category": category}
    products.append(new_product)
    save_products(products)
    print("Product added successfully!")
    return True

def list_products(products):
    print("----------Products----------")
    for product in products:
        print(f"Name: {product['name']}")
        print(f"Price: R {product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f"Category: {product['category']}")
        print("-" *20)
        
def update_product(products):
    list_products(products)
    name = input("Enter the name of product to update: ").strip().lower()
    
    product = find_product(products,name)
    
    if product:
        product["price"] = float(input("Enter the new price: R "))
        product["quantity"] = int(input("Enter the new quantity: "))
        save_products(products)
        print("Product updated successfully!")
        return True
        
    print("product not found")
    return False

def delete_product(products):
    list_products(products)
    name =input("Enter the name of the product you want to delete: ").strip().lower()
    
    product = find_product(products,name)
    
    if product:
        products.remove(product)
        save_products(products)
        print("Product has been deleted!")
        return True
    return False

def find_product(products, name):
    for product in products:
        if name.lower() == product["name"].lower():
            return product
    return None

def search_product(products):
    name =input("Enter the name of the product you want to search: ").strip().lower()
    product = find_product(products,name)
    
    if product:
        print(f"Name: {product['name']}")
        print(f"Price: R {product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f"Category: {product['category']}")
    else:
        print("product not found")
    

        
            
    