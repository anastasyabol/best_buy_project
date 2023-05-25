import products

class Store:
    """defining new class Store, that contains Product objects"""

    def __init__(self, product):
        """product is a list of Product objects"""
        self.product = product

    def add_product(self, product):
        """add product to the store"""
        self.product.append(product)

    def remove_product(self, product):
        """remove product from the store"""
        self.product.remove(product)

    def get_total_quantity(self):
        """Prints total amount of all product in the store"""
        total = 0
        for item in self.product:
            total += item.quantity
        print(f'Total of {total} items in store')

    def get_all_products(self):
        """creates a list of only active items"""
        active_list = []
        for item in self.product:
            if item.active == True:
                active_list.append(item)
        return active_list

    def print_all_active_products(self):
        active_list = self.get_all_products()
        for i, item in enumerate(active_list):
            print(f'{i+1}. {item}')


    def order(self, shopping_list):
        """ordering item/s. shopping_list is a tuple of product and amount"""
        price = 0
        for item, quantity in shopping_list:
            price += item.buy(quantity)
        return price

    def get_order(self):
        order_list = []
        active_list = self.get_all_products()
        user_item = None
        while True:
            user_item = input("When you want to finish order, enter empty text. \n Which # procuct do you want? ")
            if user_item == "":
                break
            else:
                if not 0 < int(user_item) <= len(active_list):
                    print("Wrong item. Please start over")
                    continue
                user_quantity = int(input("What amount do you want? "))
                if 0 < user_quantity <= active_list[int(user_item) - 1].quantity:
                    order_list.append((active_list[int(user_item) - 1], user_quantity))
                else:
                    print("Wrong quantity, try again")
        total_order = self.order(order_list)
        print(f"Total order amount is {total_order}")