class Product:
    def __init__(self, name, price, quantity):
        """creates new Product object. name: str, price: float, quantity: int
        set_quantity creates self.active and sets it to True if its >0"""
        self.name = name
        if not name:
            raise ValueError("Wrong name")
        try:
            float(price)
        except ValueError:
            raise ValueError("Price must be an int or float")
        self.price = float(price)
        if type(quantity) != int:
            raise ValueError("Quantity must be an int")
        self.set_quantity(quantity)
        if self.price <= 0 or self.quantity <= 0:
            raise ValueError("Wrong amount")

    def __repr__(self):
        """changes the representation while printing to the name/price/quantity"""
        return f'{self.name}, Price: {self.price}, Quantity:{self.quantity}'

    def get_quantity(self):
        """returns quantity of the product"""
        return self.quantity

    def set_quantity(self, quantity):
        """sets quantity of the product and sets active accordingly"""
        self.quantity = quantity
        self.active = self.quantity > 0

    def is_active(self):
        """returns active status"""
        return self.active == True

    def activate(self):
        """changes active to True"""
        self.active = True
        return self.active

    def deactivate(self):
        """changes active to False"""
        self.active = False
        return self.active

    def show(self):
        """showing products details"""
        print(f'{self.name}, Price: {self.price}, Quantity: {self.quantity} ')

    def buy(self, quantity):
        """buying item if it's active, changes total quantity and returns the price"""
        if self.active == False:
            print("Sorry, this item isn't active")
        else:
            if quantity > self.quantity:
                return f"Wrong quantity! Availivle amount is {self.quantity}"
            else:
                self.set_quantity(self.quantity-quantity)
                return self.price * quantity
