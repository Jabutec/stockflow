from modules.products import products ,add_product, list_products, update_product,handle_search,delete_product
from modules.sales import sales, sell_product, view_sales
from modules.customers import customers , add_customer, list_customers, delete_customer, handle_customer_search
from reports import sales_summary, generate_report

while True:
    print("-----Business Management System-----")
    print("1. Add products")
    print("2. List products")
    print("3. Update products")
    print("4. Delete products")
    print("5. Search products")
    print("6. Sell products")
    print("7. View Sales")
    print("8. Add customer")
    print("9. list customers")
    print("10. delete customer")
    print("11. Search customer")
    print("12. Generate report")
    print("13. Exit")
    
    
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
        sell_product(products,customers, sales)
    elif choice == "7":
        view_sales(sales)
    elif choice == "8":
        add_customer(customers)
    elif choice == "9":
        list_customers(customers)
    elif choice == "10":
        delete_customer(customers)
    elif choice == "11":
        handle_customer_search(customers)
    elif choice == "12":
        generate_report(sales)
    elif choice == "13":
        print("Exiting...")
        break
    else:
        print("invalid choice.")  