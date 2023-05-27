import products
import store
import promotions

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1000, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=100),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[2].set_promotion(thirty_percent)

#creating new store
best_buy = store.Store(product_list)


#functions_dictionary:
func_dict = {1: best_buy.print_all_active_products, 2: best_buy.get_total_quantity, 3: best_buy.get_order, 4: quit}


def menu():
    """prints menu and user selection"""
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



