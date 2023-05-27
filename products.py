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
            raise TypeError("Quantity must be an int")
        self.set_quantity(quantity)
        if self.price <= 0 or self.quantity <= 0:
            raise ValueError("Wrong amount")
        self.promotion = None


    def __repr__(self):
        """changes the representation while printing to the name/price/quantity"""
        return f'{self.name}, Price: {self.price}, Quantity:{self.quantity}. Promotion: {self.promotion}'

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
        print(self)

    def buy(self, quantity):
        """buying item if it's active, changes total quantity and returns the price"""
        if quantity > self.quantity:
            raise ValueError(f"Wrong quantity! Amount higher than availible quantity: {self.quantity}")
        elif self.active == False:
            print("Sorry, this item isn't active")
        elif self.promotion is not None:
            self.set_quantity(self.quantity - quantity)
            return self.promotion.apply_promotion(self, quantity)
        else:
            self.set_quantity(self.quantity - quantity)
            return self.price * quantity

    def get_promotion(self):
        """returns if there is a promotion"""
        return self.promotion
    def set_promotion(self, promotion):
        """sets promotion"""
        self.promotion = promotion



class NonStockedProduct(Product):
    """Creates non-stocked product with self.quantity = 0"""
    def __init__(self, name, price):
        super().__init__(name, price, quantity=1)
        self.quantity = 0

    def __repr__(self):
        """changes the representation while printing to the name/price/quantity"""
        return f'{self.name}, Price: {self.price}, Quantity: Unlimited. Promotion: {self.promotion}'

    def buy(self, quantity):
        """buying item if it's active, changes total quantity and returns the price"""
        if not self.active:
            print("Sorry, this item isn't active")
        elif quantity <= 0:
            raise ValueError("Wrong quantity, must be positive")
        elif self.promotion is not None:
            return self.promotion.apply_promotion(self, quantity)
        else:
            return self.price * quantity

class LimitedProduct(Product):
    """Creates limited product with default maximum 1 value. This value can't be exceded during the order"""
    def __init__(self, name, price, quantity, maximum=1):
        super().__init__(name, price, quantity)
        self.maximum_count = maximum
        self.maximum_print = maximum

    def __repr__(self):
        """changes the representation while printing to the name/price/quantity"""
        return f'{self.name}, Price: {self.price}, Limited to {self.maximum_print} per order!'

    def reset_max_count(self):
        self.maximum_count = self.maximum_print
        return self.maximum_count