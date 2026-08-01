import json

def load_customers():
    try:
        with open("customers.json", "r") as file:
            customers = json.load(file)
            return customers
    except FileNotFoundError:
        return []
    
def save_customers(customers):
    try: 
        with open("customers.json", "w") as file:
            json.dump(customers, file, indent=4)
    except Exception as e:
        print(f"Error saving product {e}")
        
customers = load_customers()

def add_customer(customers):
    name = input("Enter the name of the customer: ").strip()
    phone = input("Enter customer phone number: ").strip()
    email = input("Enter customer email address: ").strip()
    
    new_customer = {"name": name, "phone": phone, "email": email}
    customers.append(new_customer)
    save_customers(customers)
    print("Customer added successfully!")
    return True

def list_customers(customers):
    print("-----------Customers-----------")
    for customer in customers:
        print(f"Name: {customer['name']}")
        print(f"Phone: {customer['phone']}")
        print(f"Email: {customer['customer']}")
        print("-" * 20)
        
def find_customer(customers, name):
    for customer in customers:
        if name.lower() == customer["name"].lower():
            return customer
    return None