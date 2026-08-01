from products import products, add_product, list_products, update_product,search_product,delete_product
from sales import sales, sell_product

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