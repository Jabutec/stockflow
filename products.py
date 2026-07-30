products = [
    {"name" : "milk", "price": 20.00, "quantity": 50, "category": "dairy"},
    {"name" : "Bread", "price": 22.25, "quantity": 25, "category": "bakery"},
    {"name" : "popcorn", "price": 15.00, "quantity": 100, "category": "snacks"},
    {"name" : "juice", "price": 18.00, "quantity": 70, "category": "beverages"},
]


def add_product(products):
    product_name = input("Enter the name of product: ").strip().lower()
    price = float(input("Enter the price of the product: ").strip())
    quantity = int(input("Enter the number of products: "))
    category = input("Enter the category of the product: ").strip().lower()
    
    new_product = {"name" : product_name, "price": price, "quantity": quantity, "category": category}
    products.append(new_product)
    
    return True

def list_products(products):
    print("----------Products----------")
    for product in products:
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f"Category: {product['category']}")
        print("-" *20)
        
def update_products(products):
    list_products(products)
    name = input("Enter the name of product to update: ").strip().lower()
    
    product = find_product(products,name)
    
    if product:
        product["price"] = float(input("Enter the new price: "))
        product["quantity"] = int(input("Enter the new quantity: "))
        print("Product updated successfully!")
        return True
        
    print("product not found")
    return False

def delete_product(products,):
    list_products(products)
    name =input("Enter the name of the product you want to delete: ").strip().lower()
    
    product = find_product(products,name)
    
    if product:
        products.remove(product)
        return True
    return False

def find_product(products, name):
    for product in products:
        if name.lower() == product["name"].lower():
            return product
    return None

def search_product(products):
    name =input("Enter the name of the product you want to delete: ").strip().lower()
    product = find_product(products,name)
    
    if product:
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f"Category: {product['category']}")
        

while True:
    print("-----Business Management System-----")
    print("1. Add products")
    print("2. List Products")
    print("3. Update products")
    print("4. Delete products")
    print("5. Exit")
    
    
    choice = input("Enter you choice: ")
    
    if choice == "1":
        add_product(products)
    elif choice == "2":
        list_products(products)
    elif choice == "3":
        update_products(products)
    elif choice == "4":
        delete_product(products)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("invalid choice.")          
            
    