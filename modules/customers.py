import json

def load_customers():
    try:
        with open("data/customers.json", "r") as file:
            customers = json.load(file)
            return customers
    except FileNotFoundError:
        return []
    
def save_customers(customers):
    try: 
        with open("data/customers.json", "w") as file:
            json.dump(customers, file, indent=4)
    except Exception as e:
        print(f"Error saving product {e}")

def generate_customer_id(customers):
    if customers:
        return max(customer["id"] for customer in customers) + 1
    else: 
        return 1
        
customers = load_customers()

def add_customer(customers):
    name = input("Enter the name of the customer: ").strip()
    phone = input("Enter customer phone number: ").strip()
    email = input("Enter customer email address: ").strip()
    
    new_customer = {
        "id": generate_customer_id(customers),
        "name": name,
        "phone": phone,
        "email": email
    }
    customers.append(new_customer)
    save_customers(customers)
    print("Customer added successfully!")
    return True

def list_customers(customers):
    print("-----------Customers-----------")
    for customer in customers:
        print(f"ID: {customer['id']}")
        print(f"Name: {customer['name']}")
        print(f"Phone: {customer['phone']}")
        print(f"Email: {customer['email']}")
        print("-" * 20)
        
def find_customer(customers, customer_id):
    for customer in customers:
        if customer_id == customer["id"].lower():
            return customer
    return None

def delete_customer(customers):
    customer_id = input("Enter the id of the customer to delete: ")
    
    customer = find_customer(customers, customer_id)
    
    if customer:
        customers.remove(customer)
        print("Customer has been deleted!")
        return True
    return False

def search_customer(customers, name):
    matches = []
    for customer in customers:
        if name.lower() in customer["name"]:
            matches.append(customer["name"])
    return matches


        