import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                ]

#creating new store
best_buy = store.Store(product_list)


#functions_dictionary:
func_dict = {1: best_buy.print_all_active_products, 2: best_buy.get_total_quantity, 3: best_buy.get_order, 4: quit}


def menu():
    print("""
        Store Menu
       ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit
    """)
    user = ""
    while True:
        user = input("Please chose menu number: ")
        if user == "1" or user == "2" or user == "3" or user == "4":
            func_dict[int(user)]()

def main():
    menu()

if __name__ == '__main__':
    main()



