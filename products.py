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
    
    
products = load_products()
sales = load_sales()
    
    
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

    

while True:
    print("-----Business Management System-----")
    print("1. Add products")
    print("2. List Products")
    print("3. Update products")
    print("4. Delete products")
    print("5. Search Products")
    print("6. Sell Products")
    print("7. Exit")
    
    
    choice = input("Enter you choice: ")
    
    if choice == "1":
        add_product(products)
    elif choice == "2":
        list_products(products)
    elif choice == "3":
        update_product(products)
    elif choice == "4":
        delete_product(products)
    elif choice == "5":
        search_product(products)
    elif choice == "6":
            sell_product(products,sales)
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("invalid choice.")          
            
    