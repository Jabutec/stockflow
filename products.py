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
        
def generate_next_id(products):
    if products:
        return max(product["id"] for product in products) + 1
    else:
        return 1
    
products = load_products()

def add_product(products):
    product_name = input("Enter the name of product: ").strip().lower()
    price = float(input("Enter the price of the product: ").strip())
    quantity = int(input("Enter the number of products: "))
    category = input("Enter the category of the product: ").strip().lower()
    
    new_product = {
        "id" : generate_next_id(products),
        "name" : product_name, 
        "price": price, 
        "quantity": quantity, 
        "category": category
    }
    products.append(new_product)
    save_products(products)
    print("Product added successfully!")
    return True

def list_products(products):
    print("----------Products----------")
    for product in products:
        print(f"id: {product['id']}")
        print(f"Name: {product['name']}")
        print(f"Price: R {product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print(f"Category: {product['category']}")
        print("-" *20)
        
def update_product(products):
    list_products(products)
    product_ID = int(input("Enter the name of product to update: ").strip().lower())
    
    product = find_product(products,product_ID)
    
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
    product_ID = int(input("Enter the ID of the product you want to delete: "))
    
    product = find_product(products,product_ID)
    
    if product:
        products.remove(product)
        save_products(products)
        print("Product has been deleted!")
        return True
    return False

def find_product(products, product_ID):
    for product in products:
        if product_ID == product["id"]:
            return product
    return None


def search_product(products,name):
    matches = []
    for product in products:
        if name.lower() in product['name'].lower():
            matches.append(product['name'])
    return matches
    

def handle_search(products):
    name =input("Enter the name of the product you want to search: ").strip().lower()
    results = search_product(products,name)
    
    if results:
        for product in products:
            print(f"Id: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: R {product['price']:.2f}")
            print(f"Quantity: {product['quantity']}")
            print(f"Category: {product['category']}")
    else:
        print("product not found")
    

        
            
    