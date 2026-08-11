import json
from utils.validators import is_valid_name, is_valid_phone, is_valid_email, is_postive_integer
from utils.helpers import find_customer

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
    if not is_valid_name(name):
        print("Invalid name")
        return
    
    
    phone = input("Enter customer phone number: ").strip()
    if not is_valid_phone(phone):
        print("Invalid phone number")
        return
    
    email = input("Enter customer email address: ").strip()
    if not is_valid_email(email):
        print("Invalid email address")
        return
    
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
        


def delete_customer(customers):
    customer_id = input("Enter the id of the customer to delete: ")
    if not is_postive_integer(customer_id):
        print("Customer not found")
        return
    
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
            matches.append(customer)
    return matches


        