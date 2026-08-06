from modules.products import products ,add_product, list_products, update_product,handle_search,delete_product
from modules.sales import sales, sell_product
from modules.customers import customers , add_customer, list_customers, delete_customer

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
        handle_search(products)
    elif choice == "6":
        sell_product(products,sales)
    elif choice == "7":
        add_customer(customers)
    elif choice == "8":
        list_customers(customers)
    elif choice == "9":
        delete_customer(customers)
    elif choice == "10":
        print("Exiting...")
        break
    else:
        print("invalid choice.")  