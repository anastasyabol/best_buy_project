from abc import ABC, abstractmethod
import products
import store

class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class SecondHalfPrice(Promotion):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'{self.name}'
    def apply_promotion(self, product, quantity):
        discount_price = product.price * quantity / 2 * 1.5
        if quantity % 2 == 0:
            return discount_price
        else:
            return discount_price + product.price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'{self.name}'
    def apply_promotion(self, product, quantity):
        if quantity % 3 == 0:
            return product.price * quantity / 3 * 2
        else:
            return (product.price * quantity / 3 * 2) + (quantity % 3 * product.price)

class PercentDiscount():
    def __init__(self, name, percent):
        self.name = name
        self.percent = (100 - percent) / 100

    def __repr__(self):
        return f'{self.name}'
    def apply_promotion(self, product, quantity):
        return product.price * quantity * self.percent